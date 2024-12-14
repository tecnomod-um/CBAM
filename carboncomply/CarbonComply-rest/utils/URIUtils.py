class URIUtils:

    @staticmethod
    def get_name_from_uri(uri: str):
        start_name = max(uri.rfind('/'), uri.rfind('#')) + 1
        name = uri[start_name:]
        return name
