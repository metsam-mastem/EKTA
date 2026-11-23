# Initial Knowledge Graph Model

```mermaid
flowchart LR
 D[Engineering Domain] -->|classifies| C[Concept]
 L[Engineering Layer] -->|locates| C
 T[Knowledge Type] -->|types| C
 C -->|uses| TEC[Technique]
 C -->|implemented by| I[Implementation]
 C -->|specified by| S[Standard]
 C -->|depends on| DEP[Dependency]
 SRC[Source] -->|supports| CLAIM[Claim]
 CLAIM -->|qualifies| C
 DEC[Decision] -->|selects/rejects| ALT[Alternative]
 TEST[Test] -->|verifies| CLAIM
```

Each edge should include subject ID, predicate, object ID, context, source/evidence ID, status, date, and optional version scope.

Future exports: JSON, JSON-LD, RDF/Turtle, GraphML, CSV node/edge tables, SVG/PNG. Generated outputs must be reproducible and identify source revision.
