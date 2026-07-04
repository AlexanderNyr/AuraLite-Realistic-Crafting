# 📝 AuraLite Realistic Crafting — Changelog

## [0.1.2] - 2026-07-04
### 🚀 Major Improvements & New Features (42 New Recipes! Total: 1300 Recipes)
- **New Realistic Crafting Recipes:**
  - `Bell` — Craftable bell using 3 gold ingots, an iron block clapper, and a stone slab base.
  - `Trident` — Realistic marine weapon crafting using 3 prismarine shards, 2 prismarine crystals, and a stick.
  - `Bundle` — Craftable storage bag using 3 leather, 2 string, and an iron nugget clasp.
  - `Cobweb` — Decorative cobweb crafting from 5 string in an X pattern.
  - `Name Tag` — Craftable name tag using paper, string, and a copper nugget clasp.
  - `Phantom Membrane` — Bio-leather synthesis from 2 leather and fermented spider eye (enables elytra repair without phantom farming).
  - `Elytra Repair` — Shapeless repair recipe combining elytra with phantom membrane and leather.
  - `Starch Slime Ball` — Alternative adhesive slime ball recipe from wheat, water bucket, and lime dye.
  - `Magma Cream Slime Ball` — Cooling magma cream with water into a slime ball.
  - `Gravel Crushing & Reconstitution` — Crushing 4 gravel into 4 flint, and reconstituting flint with dirt back into gravel.
  - `Bamboo Paper Pulp` — Crafting 2 paper from 3 bamboo and a water bucket.
  - `Rotten Flesh Curing` — Smelting or smoking rotten flesh on a campfire or smoker converts it into leather!
  - `Heavy Padded Saddle` — Enhanced heavy saddle recipe using wool padding, leather, and iron ingots.
- **Expanded Heavy Metal & Armor Recycling (Smelting & Blasting):**
  - `Horse Armor Recycling` — Blasting iron, golden, and diamond horse armor returns iron ingots, gold ingots, and diamonds respectively; smelting leather horse armor returns leather.
  - `Minecart & Rail Recycling` — Blasting all minecart variants (chest, hopper, tnt, furnace, standard) returns iron ingots.
  - `Heavy Metal Block Recycling` — Blasting cauldrons, damaged/chipped/normal anvils, hoppers, and pressure plates returns iron blocks or ingots.
  - `Architectural Metal Recycling` — Smelting iron doors, trapdoors, iron bars, chains, lanterns, and soul lanterns returns iron ingots/nuggets.
  - `Bell & Trident Recycling` — Blasting bells returns gold ingots; blasting tridents returns prismarine shards.
  - `Armor Stand & Name Tag Recycling` — Smelting returns smooth stone slabs and iron nuggets.

### 🛠️ Tooling & Build System Overhaul (100x Speedup)
- **Build Speed:** Replaced slow bash-loop JSON tool checking with direct Python AST/JSON validation, reducing build and validation time from ~50 seconds down to <0.5 seconds (100x faster build without timeouts).
- **Validator Precision:** Added 15 missing vanilla log, stem, flower, and slab tags to `KNOWN_TAGS` in `validate_recipes.py`, eliminating false-positive errors on wood plank recipes.
- **Archive Integrity:** Fixed missing documentation bundling in `package.sh` so `README.md`, `LICENSE.txt`, `CHANGELOG.md`, and `pack.png` are properly copied into every Datapack (`.zip`), Fabric (`.jar`), and Forge (`.jar`) archive.
- **File Naming Standards:** Renamed confusing `string_from_string_alt.json` to `string_from_cobweb.json` and standardized `enchanted_golden_apple_unobtainable.json` to `enchanted_golden_apple.json`.

---

## [0.1.1] - 2026-07-04
- **New recipes:**
  - `Brush` (1.20) — realistic archaeological brush: feather/stick/copper + alternate rabbit-hide variant
  - `Calibrated Sculk Sensor` — enhanced recipe requiring redstone tuning
  - `Recycle Brush` — dismantle brushes back into copper nuggets
  - `Recycle Spyglass` — dismantle spyglasses back into copper nuggets
  - `Recycle Compass / Clock` — dismantle back into iron/gold nuggets
  - `Recycle Saddle / Crossbow / Bow / Shears / Bucket / Flint & Steel` — smelting returns materials
  - `Recycle Lead` — unravel back into string
  - `Beehive` — realistic woodworking recipe with honeycomb
- **Build system & Bug Fixes:**
  - Added JSON validation and duplicate-ID detection in `scripts/package.sh`
  - Corrected `Enchanted Golden Apple` result item and balanced `Anvil` recipe cost
  - Removed duplicate recipes: `locator_map`, `white_wool_alt`, `empty_map_v2`

---

## [0.1.0-beta] - 2026-07-04
- Initial release with 1247 realistic recipes covering tools, armor, dyes, stone, redstone, food, transport, magic, recycling and more.
