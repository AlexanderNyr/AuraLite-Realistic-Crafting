# Changelog — AuraLite Realistic Crafting

## v0.1.1

### New Recipes
- **Brush** (Minecraft 1.20) — archaeological brush crafted from feather + stick + copper ingot, plus an alternate recipe using rabbit hide for the bristles.
- **Calibrated Sculk Sensor** — enhanced recipe that adds redstone dust to the vanilla sculk sensor + amethyst shards, reflecting the calibration/tuning process.
- **Recycle Brush** — shapeless dismantling of a brush back into copper nuggets.
- **Recycle Spyglass** — shapeless dismantling of a spyglass back into copper nuggets.
- **Recycle Compass** — shapeless dismantling of a compass back into 4 iron nuggets.
- **Recycle Clock** — shapeless dismantling of a clock back into 4 gold nuggets.

### Bug Fixes (from v0.1.0)
- **Enchanted Golden Apple** — fixed result item: was incorrectly set to `minecraft:golden_apple` instead of `minecraft:enchanted_golden_apple`.
- **Anvil** — fixed recipe cost: was absurdly requiring 7 iron blocks (63 ingots). Restored to vanilla-like 3 iron blocks + 4 iron ingots.
- **Removed duplicates** — deleted `locator_map.json` (identical to `map.json`), `white_wool_alt.json` (identical to `white_wool.json`), and `empty_map_v2.json` (Bedrock-only recipe).
- **Removed misleading recipe** — deleted `apple_pie.json` which produced `pumpkin_pie` under a confusing filename.
- **Recycle Saddle (Blast)** — blast furnaces turn saddles back into iron nuggets.
- **Recycle Crossbow (Blast)** — blast furnaces turn crossbows back into iron nuggets.
- **Recycle Bow (Blast)** — blast furnaces turn bows back into leather scraps.
- **Recycle Lead** — unravel leads back into 2 string.
- **Recycle Bucket / Shears / Flint & Steel (Blast)** — smelt iron-based tools back into iron nuggets.
- **Beehive** — realistic woodworking recipe using planks and honeycomb.

### Build System Improvements
- `scripts/package.sh` now validates **every JSON recipe** with `python3 -m json.tool` before packaging.
- Added **duplicate recipe filename detection** to prevent ID collisions.
- Fabric `fabric.mod.json` updated with `contact` block (homepage + sources) and refreshed dependency ranges.
- Forge `mods.toml` updated with `issueTrackerURL`, `displayURL`, and more descriptive credits.
- `CHANGELOG.md` is now included inside every generated archive (datapack, Fabric, Forge).

### Quality & Maintenance
- Total recipe count raised from **1247 → 1258** (после удаления дублей и багов).
- All README download links and version references updated to `0.1.1`.
- `pack.mcmeta` descriptions dynamically include the live recipe count.

---

## v0.1.0-beta

- Initial release.
- **1247 realistic recipes** replacing almost every vanilla crafting, smelting, blasting, and smithing recipe in Minecraft 1.20.1.
- Covers: wood, tools, armor, dyes, stone, copper, lighting, utility blocks, redstone, transport, weapons, food, magic, recycling, fireworks, glass, and nature blocks.
- Shipped in three formats: vanilla datapack, Fabric mod, Forge mod.
