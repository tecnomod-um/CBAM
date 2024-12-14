import re


def normalize(text: str) -> str:
    """
    Normalize a header by converting it to lowercase, replacing spaces and parentheses with underscores,
    and removing any redundant underscores.
    """
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with underscores
    text = text.replace(' ', '_')
    # Replace parentheses with underscores
    text = text.replace('(', '_').replace(')', '_').replace(',', '').replace('\n\r', '').replace('\n', '')
    # Remove any leading/trailing whitespace and redundant underscores
    text = re.sub(r'_+', '_', text).strip('_')
    return text

def normalize_list(l: list) -> list:
    new_list = []
    for element in l:
        new_list.append(normalize(element))
    return new_list

def remove_non_numeric_characters(text: str) -> str:
    return re.sub("[^\d\.]", "", text).strip()
