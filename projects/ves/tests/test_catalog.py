import unittest
from ves_catalog import DEFAULT_CATALOG, DeckDefinition, search_card_types, validate_deck


class CatalogTests(unittest.TestCase):
    def test_search_returns_reusable_card_type_definitions(self):
        results = search_card_types(DEFAULT_CATALOG, query="sensor", category="hardware")
        self.assertTrue(results)
        self.assertEqual(results[0].type_id, "hardware.sensor")

    def test_default_decks_reference_known_card_types(self):
        for deck in DEFAULT_CATALOG.decks:
            self.assertEqual(validate_deck(DEFAULT_CATALOG, deck), [])

    def test_invalid_deck_reference_is_reported(self):
        deck = DeckDefinition("deck.bad", "Bad Deck", ("hardware.unknown",))
        self.assertEqual(validate_deck(DEFAULT_CATALOG, deck), ["hardware.unknown"])


if __name__ == "__main__":
    unittest.main()
