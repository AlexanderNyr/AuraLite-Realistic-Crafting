# ✨ AuraLite Realistic Crafting — Minecraft 1.20.1

**Copyright © 2026 AlexanderNyr** · License: **CC BY‑NC‑SA 4.0**

**1300 reworked recipes** — almost every vanilla craft is now more realistic.
Ships in **3 formats**: vanilla **datapack**, **Fabric** mod, **Forge** mod.

![icon](icon.png)

> 📜 **TL;DR license:** You may freely use, modify and redistribute this mod **with credit to AlexanderNyr** and **only for non‑commercial purposes**; derivative works must use the same license. Full text in `LICENSE.txt`. **Monetized YouTube/Twitch videos are fine** — see the Rules & Permissions section below.

---

## 📦 Downloads (`build/` folder)

| File | Where to put it | Requires |
|---|---|---|
| `AuraLiteRealisticCrafting-datapack-0.1.2.zip` | `<world>/datapacks/` | nothing — vanilla 1.20.1 client |
| `AuraLiteRealisticCrafting-fabric-0.1.2.jar`   | `.minecraft/mods/` | Fabric Loader 0.14+ |
| `AuraLiteRealisticCrafting-forge-0.1.2.jar`    | `.minecraft/mods/` | Forge 47+ |

> The datapack is a `.zip` (Minecraft data packs require this), while Fabric/Forge mods **must** be `.jar` files — the loaders ignore anything else in the `mods/` folder. All three files contain the same JSON recipes; only the manifest differs.

---

## 🚀 Installation

### Datapack (no mods needed, any 1.20.1 client)
1. Put `AuraLiteRealisticCrafting-datapack-0.1.2.zip` into `<world_folder>/datapacks/`.
2. Enter the world and run `/reload`. Verify with `/datapack list`.

### Fabric
1. Install [Fabric Loader 0.14+](https://fabricmc.net/use/installer/) for 1.20.1.
2. Drop `AuraLiteRealisticCrafting-fabric-0.1.2.jar` into `.minecraft/mods/`.
3. Launch the Fabric profile.

### Forge
1. Install [Forge 47.x](https://files.minecraftforge.net/) for 1.20.1.
2. Drop `AuraLiteRealisticCrafting-forge-0.1.2.jar` into `.minecraft/mods/`.
3. Launch. The mod registers via `lowcodefml` (pure data — no Java code).

Works on servers too — same file goes into the server's `mods/` folder or world `datapacks/` folder.

---

## 🛠 What changed (1300 recipes)

### 🪵 Wood (11 types: oak, spruce, birch, jungle, acacia, dark_oak, mangrove, cherry, crimson, warped, bamboo)
- **1 log → 6 planks** (realistic sawmilling)
- **3 planks → 9 slabs** (a slab is half a block — more makes sense)
- **6 planks → 8 stairs**
- Doors, trapdoors, fences, gates, buttons, pressure plates, signs, boats, chest‑boats — all rebalanced
- **Hanging signs** (1.20+) for every wood type
- **Bark stripping by crafting**: log + stick → stripped log
- **Bamboo Paper Pulp**: 3 bamboo + water bucket → 2 paper

### ⛏ Tools & Weapons (6 materials: wood, stone, iron, gold, diamond, netherite)
- All tools use a **stick handle**
- Metal/diamond/netherite tools **also require leather** for a grip wrap on the handle
- Pickaxes, axes, shovels, hoes, swords
- **Netherite upgrades** via smithing transform (vanilla path)
- **Trident**: Craftable using 3 prismarine shards, 2 prismarine crystals, and a stick
- **Bow & Crossbow**: Rebalanced with leather grips and hook mechanisms
- **Arrows**: flint + stick + feather → **8 arrows** (was 4)

### 🛡 Armor & Survival Utility
- **Leather** — classic, unchanged; **cured from rotten flesh** on campfires or smokers!
- **Iron, gold, diamond** — require **leather padding** (gambeson) inside the metal frame
- **Diamond** — extra iron fittings on helmet & chestplate
- **Chainmail** — now craftable from **chains**
- **Horse armor** (iron, gold, diamond) — now craftable and fully recyclable!
- **Shield** — leather + iron rim
- **Bundle** — craftable storage bag from leather, string, and iron nugget clasp
- **Phantom Membrane** — synthesized from leather and fermented spider eye for easy elytra repair
- **Elytra Repair** — shapeless repair variant combining damaged elytra with phantom membrane and leather

### 🎨 16 colors — full coverage
For each of the 16 vanilla colors:
- **Concrete powder** (8 sand + dye → 8)
- **Dyed terracotta** (8 terracotta + dye → 8)
- **Glazed terracotta** via furnace + blast furnace
- **Stained glass + panes** (multiple paths)
- **Dyed wool, carpets, candles, beds, banners**
- **Shulker boxes** in all colors (and reset back to plain)
- **Candle cakes** for every color
- **Banner patterns** (Creeper, Flower, Skull, Mojang, Globe)

### 🌸 Dyes & Alchemy — every source
35+ recipes: flowers (single + tall), color mixing, bone meal, lapis lazuli, cocoa, ink sac, beetroot, dried kelp, etc.
- **Starch & Magma Slime Balls**: craft slime balls from wheat + water + lime dye, or magma cream + water!

### 🟧 Copper — every oxidation stage
- `cut_copper` in all 4 stages + slabs + stairs
- **Waxing** (12 recipes using honeycomb)
- **Lightning rod**

### 🧱 Stone & Minerals (40+ blocks)
- **All slabs: 3 → 9** (was 6)
- **All stairs: 6 → 8** (was 4)
- **All walls: 6 → 9**
- **Chiseled variants** via 2 stacked slabs
- **Cracked variants** via smelting normal bricks
- **Polished, smooth, cut** variants rebalanced
- **Gravel Crushing & Reconstitution**: crush 4 gravel into 4 flint, or mix flint with dirt back into gravel
- **Stonecutter** support: 100+ recipes across 17 stone families

### 🔥 Lighting & fire
- **Torch: coal on top of stick → 2 torches** (was 4)
- **Soul torch** (2 paths), **redstone torch**, **soul lantern**
- **Campfire**: sticks + log + coal
- **Lantern / soul lantern**: 8 nuggets around a torch
- **Candle**: string + honeycomb
- **TNT**: gunpowder cross + sand corners
- **Charcoal** from all 11 wood types (smelting)

### 🏠 Utility blocks & Decorative Extras
- **Crafting table**: 4 planks + 2 sticks (legs)
- **Furnace**: 8 cobblestone + clay ball (mortar) in the center
- **Blast furnace, smoker, smithing/cartography/fletching tables, loom, stonecutter** — realistic builds
- **Bell**: craftable from 3 gold ingots, iron block clapper, and stone slab base
- **Cobweb**: craftable from 5 string in an X pattern
- **Name Tag**: craftable from paper, string, and copper/iron nugget clasp
- **Chest** with iron‑nugget hinges
- **Ender chest, shulker box, hopper, bucket, bowl** (clay-ceramic, not wood)
- **Barrel, lectern, bookshelf** (with actual books), **armor stand**
- **Decorated pot** (1.20+), **Chiseled bookshelf** (1.20+)

### ⚙ Redstone & Transport
- **Piston, sticky piston, observer**, **Repeater, comparator** rebuilt with real torches
- **Redstone lamp, daylight detector**, **Calibrated Sculk Sensor**
- **Rails**: 24 per craft (was 16)
- **Minecart**: 5 iron; all variants (chest/furnace/hopper/TNT) balanced and recyclable
- **Saddle**: heavy padded and standard variants from leather, wool, string, and iron

### 🍞 Food & Farming
- **Bread**: 3 wheat + egg + water bucket → 2 bread
- **Cookie**: wheat + cocoa → 16 (bulk pattern)
- **Cake, pumpkin pie** with alternative recipes
- **Cooking** via furnace, smoker, and campfire for every meat/fish/potato

### 🪄 Magic / enchanting
- **Enchanting table**: book + 4 diamonds + 4 obsidian
- **Anvil, beacon, end crystal, conduit, brewing stand**
- **Reinforced deepslate** — craftable from deepslate + echo + netherite
- **Froglights** (all 3 colors) — glowstone + magma cream
- **Tinted glass, calibrated sculk sensor, recovery compass**

### 💎 Ingots ↔ blocks
- 9 materials (iron, gold, diamond, emerald, lapis, redstone, coal, netherite, copper) — block ↔ ingot, both ways
- Iron/gold nuggets — convertible both ways
- **Netherite ingot** craftable from 4 scrap + 4 gold
- **Amethyst block** ↔ **amethyst shard** both ways

### ♻️ Comprehensive Eco-Recycling (Smelting & Blasting)
Don't let old gear go to waste! Almost every metal, armor, or utility item can be dismantled or melted down:
- **Horse Armor Recycling**: Blasting iron, golden, and diamond horse armor returns ingots/diamonds; smelting leather horse armor returns leather.
- **Minecart & Rail Recycling**: Blasting standard, chest, hopper, tnt, and furnace minecarts returns iron ingots.
- **Heavy Metal Block Recycling**: Blasting cauldrons, anvils (all damage states), hoppers, and metal pressure plates returns iron blocks/ingots.
- **Architectural Metal Recycling**: Smelting iron doors, trapdoors, iron bars, chains, lanterns, and soul lanterns returns metal.
- **Weapons & Tools**: Blasting tridents returns prismarine shards; blasting bells returns gold ingots; diamond/netherite gear dismantles via crafting table.
- **Textiles & Utility**: Smelting armor stands and name tags returns slabs/nuggets; wool unravels to string; rotten flesh cures to leather.

---

## ⚖️ Rules & Permissions (FAQ)

**Copyright © 2026 AlexanderNyr** — licensed under **CC BY‑NC‑SA 4.0**.

- **Videos & Streams:** You are free to showcase, stream, and use this datapack/mod in your videos — **including monetized channels on YouTube, Twitch, Kick, TikTok, etc.** Showing the mod in monetized content does **not** count as "commercial use" under this license. A mention/credit in the description is appreciated but not required.
- **Modpacks:** You are free to include this datapack/mod in your **free** modpacks on CurseForge, Modrinth, Technic, or any other platform. Please keep the original credit to **AlexanderNyr** in the modpack description.
- **Personal Tweaks:** You can freely modify the recipes / code for your own personal use, your own server, or your community.
- **No Re‑hosting:** Do **not** upload the raw files to third‑party download sites (especially behind ad‑links like AdFly, Linkvertise, and similar). Always link to the official authorized source.
- **Derivative Works:** If you modify this mod/datapack and **distribute** your version publicly, your release **must** be free, open‑source, and licensed under the exact same **CC BY‑NC‑SA 4.0** license, with clear attribution to the original author **AlexanderNyr**.
- **Commercial use:** Selling the mod, paywalling access to it, including it in **paid** modpacks/servers, or any other direct commercialization is **not allowed** without explicit written permission from the author.

### License at a glance

- ✅ **BY** — give credit: **AlexanderNyr** + a link to the project.
- 🚫 **NC** — non‑commercial use. Monetized video content **is allowed**; selling the mod/datapack itself **is not**.
- 🔁 **SA** — derivative works must be released under this same CC BY‑NC‑SA 4.0 license.

Full legal text: see `LICENSE.txt` or
<https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode>.
Human‑readable summary: <https://creativecommons.org/licenses/by-nc-sa/4.0/>.

---

## 📁 Project structure

```
AuraLiteRealisticCrafting/
├── src/data/minecraft/recipes/    ← 1300 JSON recipe sources
├── scripts/
│   ├── package.sh                 ← builds all 3 archives (100x faster in v0.1.2)
│   └── validate_recipes.py        ← Python AST/JSON structural validator
├── formats/
│   ├── datapack/                  ← unpacked datapack contents
│   ├── fabric/                    ← unpacked Fabric mod contents
│   └── forge/                     ← unpacked Forge mod contents
├── build/
│   ├── AuraLiteRealisticCrafting-datapack-0.1.2.zip
│   ├── AuraLiteRealisticCrafting-fabric-0.1.2.jar
│   └── AuraLiteRealisticCrafting-forge-0.1.2.jar
├── pack.png                       ← 128×128 pixel-art "A" icon with aura
├── LICENSE.txt                    ← full CC BY-NC-SA 4.0 text
├── CHANGELOG.md                   ← complete release history
└── README.md
```

## 📝 Changelog

### v0.1.2
- **New Realistic Crafting Recipes (42 New Recipes! Total: 1300 Recipes):**
  - `Bell` — Craftable bell using 3 gold ingots, iron block clapper, and stone slab base.
  - `Trident` — Realistic marine weapon crafting using prismarine shards, crystals, and stick.
  - `Bundle` — Craftable storage bag from leather, string, and iron nugget clasp.
  - `Cobweb` — Decorative cobweb crafting from 5 string in an X pattern.
  - `Name Tag` — Craftable name tag using paper, string, and copper nugget clasp.
  - `Phantom Membrane` — Bio-leather synthesis from leather and fermented spider eye.
  - `Elytra Repair` — Shapeless repair recipe combining elytra with phantom membrane and leather.
  - `Starch Slime Ball` — Alternative adhesive slime ball recipe from wheat, water, and lime dye.
  - `Magma Cream Slime Ball` — Cooling magma cream with water into a slime ball.
  - `Gravel Crushing & Reconstitution` — Crushing 4 gravel into 4 flint, and reconstituting flint with dirt back into gravel.
  - `Bamboo Paper Pulp` — Crafting 2 paper from 3 bamboo and a water bucket.
  - `Rotten Flesh Curing` — Smelting or smoking rotten flesh on a campfire or smoker converts it into leather!
  - `Heavy Padded Saddle` — Enhanced heavy saddle recipe using wool padding, leather, and iron ingots.
- **Expanded Heavy Metal & Armor Recycling (Smelting & Blasting):**
  - `Horse Armor Recycling` — Blasting iron, golden, and diamond horse armor returns metal/gems; smelting leather horse armor returns leather.
  - `Minecart & Rail Recycling` — Blasting all minecart variants returns iron ingots.
  - `Heavy Metal Block Recycling` — Blasting cauldrons, damaged anvils, hoppers, and metal pressure plates returns iron blocks/ingots.
  - `Architectural Metal Recycling` — Smelting iron doors, trapdoors, iron bars, chains, and lanterns returns metal.
  - `Bell & Trident Recycling` — Blasting bells returns gold ingots; blasting tridents returns prismarine shards.
  - `Armor Stand & Name Tag Recycling` — Smelting returns smooth stone slabs and iron nuggets.
- **Tooling & Build System Overhaul (100x Speedup):**
  - Replaced slow bash-loop JSON tool checking with direct Python AST/JSON validation in `package.sh`, reducing build time from ~50 seconds down to <0.5 seconds.
  - Added 15 missing vanilla log, stem, flower, and slab tags to `KNOWN_TAGS` in `validate_recipes.py`, eliminating false-positive errors on wood plank recipes.
  - Fixed archive documentation bundling so `README.md`, `LICENSE.txt`, `CHANGELOG.md`, and `pack.png` are properly packaged inside every Datapack, Fabric, and Forge release.
  - Renamed confusing `string_from_string_alt.json` to `string_from_cobweb.json` and standardized `enchanted_golden_apple_unobtainable.json` to `enchanted_golden_apple.json`.

### v0.1.1
- **New recipes:** `Brush`, `Calibrated Sculk Sensor`, `Recycle Brush`, `Recycle Spyglass`, `Recycle Compass / Clock`, `Recycle Saddle / Crossbow / Bow / Shears / Bucket / Flint & Steel`, `Recycle Lead`, `Beehive`.
- **Build system & Bug Fixes:** Added JSON validation and duplicate-ID detection; corrected `Enchanted Golden Apple` result item and balanced `Anvil` recipe cost; removed duplicate recipes (`locator_map`, `white_wool_alt`, `empty_map_v2`).

### v0.1.0-beta
- Initial release with 1247 realistic recipes covering tools, armor, dyes, stone, redstone, food, transport, magic, recycling and more.

---

## 🔧 Rebuild from source

Want to tweak a recipe?

1. Edit a JSON file in `src/data/minecraft/recipes/`.
2. Run:
   ```bash
   bash scripts/package.sh
   ```
3. The built archives appear in `build/`.

## ⚙ Compatibility

- ✅ Minecraft **1.20.1** (pack_format 15)
- ✅ Fabric Loader 0.14+ / Forge 47+
- ✅ Server + client (sided = BOTH)
- ⚠️ Will conflict with other mods that override the **same** recipe IDs
- ℹ️ The in‑game recipe book picks up the new formulas automatically
