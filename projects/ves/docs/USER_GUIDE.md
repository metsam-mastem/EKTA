# VES User Guide — Initial Prototype

1. Open web/index.html in a modern browser.
2. The Architecture Board shows the sample project. Select a card to inspect it.
3. Drag cards to reposition them; the local board layout is saved in browser storage.
4. Open Card Gallery to search by name, type or category. Choose Add to board to create an instance.
5. Open Deck Library to inspect starter collections and add a complete Deck to the current board.
6. Use the Inspector to edit the selected entity's name, status and JSON properties.
7. Open Validation Lab or choose Run validation to check relationship endpoints and board references.
8. Choose Export JSON to download the current project representation.
9. Reset demo restores the sample model after confirmation.

The browser prototype is an interaction demonstration, not a production engineering validator. Its localStorage data is not encrypted or backed up. The Python core provides deeper deterministic checks and a separate SQLite persistence adapter.
