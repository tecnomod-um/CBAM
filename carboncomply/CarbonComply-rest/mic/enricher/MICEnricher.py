import copy

from mic.parser.MICParser import mic_header

mic_enriched_header = mic_header

class MICEnricher:
    def __init__(self, mic_data: dict):
        self.mic_data = mic_data

    def enrich(self) -> list:
        enriched_dict = copy.deepcopy(self.mic_data)
        return enriched_dict