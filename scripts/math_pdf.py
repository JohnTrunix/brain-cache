"""
Python Script for adding PDF Cards to different math sites
"""
import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

PDF_FILE_PATH: str = Path("./docs/math/pdf")
GENERAL_MD_FILE_PATH: str = Path("./docs/math/general.md")
ANA_MD_FILE_PATH: str = Path("./docs/math/analysis.md")
LA_MD_FILE_PATH: str = Path("./docs/math/linear-algebra.md")

# Load Jinja2 Templates
env = Environment(loader=FileSystemLoader("./scripts/templates"))
pdf_card_template = env.get_template("pdf_card.html")

def get_release_tag() -> str:
    """
    Get release tag from ./docs/math/pdf/release.txt

    :return: Release Tag as str
    """
    if Path(PDF_FILE_PATH / "release.txt").exists():
        with open(PDF_FILE_PATH / "release.txt", "r", encoding="utf-8") as file:
            return file.read().strip()
    else:
        return "None"         

def sort_files(files: list) -> list:
    """
    Sort files by tag

    :param files: List of files
    :return: Sorted list of files
    """
    files.sort(key=lambda x: x[0], reverse=False)
    for file in files:
        file[1].sort(key=lambda x: x[1], reverse=False)
    return files

def filter_files() -> tuple[list, list, list]:
    """
    Get files from PDF_FILE_PATH and filter them into LA and ANA

    :return: tuple of lists of files
    """
    release_tag = get_release_tag()
    files = []
    ana_files = {}
    la_files = {}
    general_files = {}

    for file in PDF_FILE_PATH.iterdir():
        if file.suffix == ".pdf":
            files.append([file.stem.split("_")[0], file.stem, file.name, release_tag])

    for file in files:
        tag = file[0]
        prefix = tag.rstrip("1234567890")
        if prefix == "ANA":
            if tag not in ana_files.keys():
                ana_files[tag] = []
                ana_files[tag].append(file)
            else:
                ana_files[tag].append(file)
        elif prefix == "LA":
            if tag not in la_files.keys():
                la_files[tag] = []
                la_files[tag].append(file)
            else:
                la_files[tag].append(file)
        else:
            if tag not in general_files.keys():
                general_files[tag] = []
                general_files[tag].append(file)
            else:
                general_files[tag].append(file)

    ana_files = [(tag, files) for tag, files in ana_files.items()]
    la_files = [(tag, files) for tag, files in la_files.items()]
    general_files = [(tag, files) for tag, files in general_files.items()]

    ana_files = sort_files(ana_files)
    la_files = sort_files(la_files)
    general_files = sort_files(general_files)
    
    return ana_files, la_files, general_files


def generate_html(dictionary: dict, page_title: str) -> str:
    """
    Generates HTML from templates

    :param dictionary: Dictionary of files
    :return: HTML as str
    """
    html = pdf_card_template.render(
        page_title=page_title, 
        tags=dictionary, 
        creation_date=datetime.datetime.utcnow()
    )
    return html


def write_to_md(html: str, file_path: Path) -> None:
    """
    Write genereated HTML to Markdown File

    :param html: HTML Template as str
    :param file_path: Path to Markdown File
    :param heading: Heading of Markdown File
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html)


if __name__ == "__main__":
    ana_files, la_files, general_files = filter_files()

    ana_html = generate_html(ana_files, "Analysis")
    la_html = generate_html(la_files, "Linear Algebra")
    general_html = generate_html(general_files, "General")

    write_to_md(ana_html, ANA_MD_FILE_PATH)
    write_to_md(la_html, LA_MD_FILE_PATH)
    write_to_md(general_html, GENERAL_MD_FILE_PATH)
