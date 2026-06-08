#!/usr/bin/env python3
"""
Comprehensive recipe validator for Minecraft 1.20.1 datapack recipes.
Checks: JSON validity, structure, pattern/key consistency, item/tag syntax,
recipe type validity, smelting params, and common typo patterns.
"""

import json
import os
import sys
from pathlib import Path
from collections import Counter, defaultdict

RECIPE_DIR = Path(__file__).parent.parent / "src" / "data" / "minecraft" / "recipes"

VALID_RECIPE_TYPES = {
    "minecraft:crafting_shaped",
    "minecraft:crafting_shapeless",
    "minecraft:smelting",
    "minecraft:blasting",
    "minecraft:smoking",
    "minecraft:campfire_cooking",
    "minecraft:stonecutting",
    "minecraft:smithing_transform",
    "minecraft:smithing_trim",
}

# Common 1.20.1 tags used in recipes (not exhaustive but catches most)
KNOWN_TAGS = {
    "minecraft:planks", "minecraft:logs", "minecraft:wooden_slabs",
    "minecraft:wooden_buttons", "minecraft:wooden_doors", "minecraft:wooden_stairs",
    "minecraft:wooden_trapdoors", "minecraft:wooden_pressure_plates",
    "minecraft:leaves", "minecraft:saplings", "minecraft:flowers",
    "minecraft:small_flowers", "minecraft:tall_flowers", "minecraft:wool",
    "minecraft:wool_carpets", "minecraft:beds", "minecraft:fences",
    "minecraft:wooden_fences", "minecraft:walls", "minecraft:slabs",
    "minecraft:stairs", "minecraft:doors", "minecraft:trapdoors",
    "minecraft:buttons", "minecraft:pressure_plates", "minecraft:signs",
    "minecraft:hanging_signs", "minecraft:boats", "minecraft:chest_boats",
    "minecraft:stone_crafting_materials", "minecraft:stone_tool_materials",
    "minecraft:coals", "minecraft:arrows", "minecraft:anvil",
    "minecraft:axolotl_tempt_items", "minecraft:beacon_payment_items",
    "minecraft:boats", "minecraft:candles", "minecraft:cluster_max_harvestables",
    "minecraft:compasses", "minecraft:completes_find_tree_tutorial",
    "minecraft:convertable_to_mud", "minecraft:creeper_drop_music_discs",
    "minecraft:decorated_pot_shards", "minecraft:diamond_ores",
    "minecraft:dirt", "minecraft:emerald_ores", "minecraft:fence_gates",
    "minecraft:fishes", "minecraft:gold_ores", "minecraft:iron_ores",
    "minecraft:lapis_ores", "minecraft:lectern_books", "minecraft:logs_that_burn",
    "minecraft:mangrove_logs", "minecraft:meat", "minecraft:music_discs",
    "minecraft:non_flammable_wood", "minecraft:noteblock_top_instruments",
    "minecraft:occludes_vibration_signals", "minecraft:piglin_food",
    "minecraft:piglin_loved", "minecraft:player_works_on_goat_horn",
    "minecraft:redstone_ores", "minecraft:replaceable",
    "minecraft:replaceable_by_trees", "minecraft:sand",
    "minecraft:shulker_boxes", "minecraft:sniffer_food",
    "minecraft:stone_bricks", "minecraft:stone_ore_replaceables",
    "minecraft:strider_food", "minecraft:strider_tempt_items",
    "minecraft:tall_flowers", "minecraft:terracotta",
    "minecraft:tools", "minecraft:tools/combat", "minecraft:tools/mining",
    "minecraft:tools/bows", "minecraft:tools/crossbows",
    "minecraft:tools/fishing_rods", "minecraft:tools/brushes",
    "minecraft:tools/shears", "minecraft:tools/shields",
    "minecraft:tools/maces", "minecraft:tools/swords",
    "minecraft:tools/axes", "minecraft:tools/pickaxes",
    "minecraft:tools/shovels", "minecraft:tools/hoes",
    "minecraft:torchflower_seeds", "minecraft:trapdoors",
    "minecraft:trim_materials", "minecraft:trim_templates",
    "minecraft:villager_plantable_seeds", "minecraft:wooden_tool_materials",
}

# Common typo patterns
SUSPICIOUS_PREFIXES = [
    "mincecraft", "mincraft", "minecrafts", "craft:", "mine_craft",
    "minecraft:",  # double check after colon
]

SUSPICIOUS_ITEM_NAMES = [
    "diamond_horse_armour",  # British spelling
    "iron_horse_armour",
    "gold_horse_armour",
    "leather_horse_armour",
    "color",               # should be colour in some contexts? Actually MC uses color
    "plank",               # should be planks
    "log",                 # should be logs or specific
    "ingots",              # should be ingot
    "nuggets",             # should be nugget
    "stick",               # singular is correct for item, but tag is sticks
]

def validate_item_or_tag(val, path):
    errors = []
    if not isinstance(val, str):
        errors.append(f"{path}: expected string, got {type(val).__name__}")
        return errors
    if not val.startswith("minecraft:"):
        errors.append(f"{path}: missing 'minecraft:' prefix -> '{val}'")
        return errors
    name = val[len("minecraft:"):]
    # Check for suspicious names
    if name in ["plank", "log", "ingots", "nuggets", "sticks"]:
        errors.append(f"{path}: suspicious item name '{name}' (usually singular)")
    if "_armour" in name:
        errors.append(f"{path}: British spelling 'armour' - Minecraft uses 'armor'")
    if "  " in val or val.endswith(" ") or val.startswith(" "):
        errors.append(f"{path}: whitespace issue in '{val}'")
    return errors

def validate_ingredient(ing, path):
    errors = []
    if isinstance(ing, str):
        errors.extend(validate_item_or_tag(ing, path))
    elif isinstance(ing, dict):
        if "item" in ing and "tag" in ing:
            errors.append(f"{path}: cannot have both 'item' and 'tag'")
        elif "item" in ing:
            errors.extend(validate_item_or_tag(ing["item"], f"{path}.item"))
        elif "tag" in ing:
            errors.extend(validate_item_or_tag(ing["tag"], f"{path}.tag"))
            if ing["tag"] not in KNOWN_TAGS:
                errors.append(f"{path}: unknown tag '{ing['tag']}' (may be valid, please verify)")
        else:
            errors.append(f"{path}: ingredient must have 'item' or 'tag'")
    else:
        errors.append(f"{path}: invalid ingredient type {type(ing).__name__}")
    return errors

def validate_shaped(data, filename):
    errors = []
    pattern = data.get("pattern")
    key = data.get("key")
    result = data.get("result")

    if not isinstance(pattern, list):
        errors.append("pattern must be a list of strings")
    else:
        lengths = [len(row) for row in pattern if isinstance(row, str)]
        if len(set(lengths)) > 1:
            errors.append(f"pattern rows have inconsistent lengths: {lengths}")
        if not all(isinstance(row, str) for row in pattern):
            errors.append("pattern rows must be strings")
        else:
            all_chars = set("".join(pattern))
            allowed = set(key.keys()) if isinstance(key, dict) else set()
            allowed.add(" ")
            bad = all_chars - allowed
            if bad:
                errors.append(f"pattern uses characters not in key: {bad}")
            for c in key.keys() if isinstance(key, dict) else []:
                if c == " ":
                    errors.append(f"key contains space character ' ' - use it in pattern instead")
                if len(c) != 1:
                    errors.append(f"key '{c}' is not a single character")

    if not isinstance(key, dict):
        errors.append("key must be an object")
    else:
        for k, v in key.items():
            if isinstance(v, list):
                for i, ing in enumerate(v):
                    errors.extend(validate_ingredient(ing, f"key.{k}[{i}]"))
            else:
                errors.extend(validate_ingredient(v, f"key.{k}"))

    if isinstance(result, dict):
        if "item" in result:
            errors.extend(validate_item_or_tag(result["item"], "result.item"))
        else:
            errors.append("result must have 'item'")
        if "count" in result and (not isinstance(result["count"], int) or result["count"] < 1 or result["count"] > 64):
            errors.append(f"result.count suspicious value: {result.get('count')}")
    elif isinstance(result, str):
        errors.extend(validate_item_or_tag(result, "result"))
    else:
        errors.append("result must be a string or object")

    return errors

def validate_shapeless(data, filename):
    errors = []
    ingredients = data.get("ingredients")
    result = data.get("result")

    if not isinstance(ingredients, list):
        errors.append("ingredients must be a list")
    else:
        for i, ing in enumerate(ingredients):
            errors.extend(validate_ingredient(ing, f"ingredients[{i}]"))

    if isinstance(result, dict):
        if "item" in result:
            errors.extend(validate_item_or_tag(result["item"], "result.item"))
        else:
            errors.append("result must have 'item'")
        if "count" in result and (not isinstance(result["count"], int) or result["count"] < 1 or result["count"] > 64):
            errors.append(f"result.count suspicious value: {result.get('count')}")
    elif isinstance(result, str):
        errors.extend(validate_item_or_tag(result, "result"))
    else:
        errors.append("result must be a string or object")

    return errors

def validate_smelting(data, filename):
    errors = []
    ing = data.get("ingredient")
    result = data.get("result")
    exp = data.get("experience", 0)
    time = data.get("cookingtime", 200)

    if ing is None:
        errors.append("missing 'ingredient'")
    else:
        errors.extend(validate_ingredient(ing, "ingredient"))

    if result is None:
        errors.append("missing 'result'")
    elif isinstance(result, str):
        errors.extend(validate_item_or_tag(result, "result"))
    elif isinstance(result, dict):
        if "item" in result:
            errors.extend(validate_item_or_tag(result["item"], "result.item"))
        else:
            errors.append("result must have 'item'")
    else:
        errors.append("result must be string or object")

    if not isinstance(exp, (int, float)) or exp < 0:
        errors.append(f"experience should be non-negative number, got {exp}")
    if not isinstance(time, int) or time < 1:
        errors.append(f"cookingtime should be positive int, got {time}")

    return errors

def validate_stonecutting(data, filename):
    errors = []
    ing = data.get("ingredient")
    result = data.get("result")
    count = data.get("count", 1)

    if ing is None:
        errors.append("missing 'ingredient'")
    else:
        errors.extend(validate_ingredient(ing, "ingredient"))

    if result is None:
        errors.append("missing 'result'")
    else:
        errors.extend(validate_item_or_tag(result, "result"))

    if not isinstance(count, int) or count < 1:
        errors.append(f"count should be positive int, got {count}")

    return errors

def validate_smithing(data, filename):
    errors = []
    template = data.get("template")
    base = data.get("base")
    addition = data.get("addition")
    result = data.get("result")

    for field, val in [("template", template), ("base", base), ("addition", addition)]:
        if val is None:
            errors.append(f"missing '{field}'")
        else:
            errors.extend(validate_ingredient(val, field))

    if result is None:
        errors.append("missing 'result'")
    elif isinstance(result, str):
        errors.extend(validate_item_or_tag(result, "result"))
    elif isinstance(result, dict):
        if "item" in result:
            errors.extend(validate_item_or_tag(result["item"], "result.item"))
        else:
            errors.append("result must have 'item'")
    else:
        errors.append("result must be string or object")

    return errors

def validate_file(filepath):
    errors = []
    filename = filepath.name
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"JSON decode error: {e}"]

    if not isinstance(data, dict):
        return ["root must be a JSON object"]

    rtype = data.get("type")
    if rtype is None:
        errors.append("missing 'type' field")
    elif rtype not in VALID_RECIPE_TYPES:
        errors.append(f"unknown recipe type: {rtype}")

    if rtype == "minecraft:crafting_shaped":
        errors.extend(validate_shaped(data, filename))
    elif rtype == "minecraft:crafting_shapeless":
        errors.extend(validate_shapeless(data, filename))
    elif rtype in ("minecraft:smelting", "minecraft:blasting", "minecraft:smoking", "minecraft:campfire_cooking"):
        errors.extend(validate_smelting(data, filename))
    elif rtype == "minecraft:stonecutting":
        errors.extend(validate_stonecutting(data, filename))
    elif rtype in ("minecraft:smithing_transform", "minecraft:smithing_trim"):
        errors.extend(validate_smithing(data, filename))

    return errors

def main():
    if not RECIPE_DIR.exists():
        print(f"ERROR: Recipe directory not found: {RECIPE_DIR}")
        sys.exit(1)

    files = sorted(RECIPE_DIR.glob("*.json"))
    total = len(files)
    error_count = 0
    warning_count = 0
    errors_by_file = {}
    recipe_type_counts = Counter()

    print(f"Checking {total} recipe files in {RECIPE_DIR}\n")

    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
        rtype = data.get("type", "UNKNOWN")
        recipe_type_counts[rtype] += 1

        errs = validate_file(fp)
        if errs:
            errors_by_file[fp.name] = errs
            error_count += len(errs)

    # Additional checks
    # Check for duplicate filenames (vanilla recipe IDs must be unique per namespace)
    names = [fp.stem for fp in files]
    dupes = {n: c for n, c in Counter(names).items() if c > 1}

    print("=" * 60)
    print(f"Recipe type distribution:")
    for t, c in recipe_type_counts.most_common():
        print(f"  {c:4d}  {t}")
    print()

    if dupes:
        print(f"❌ DUPLICATE FILENAMES (will overwrite each other):")
        for n, c in dupes.items():
            print(f"   {n}.json appears {c} times")
        print()

    if errors_by_file:
        print(f"❌ FOUND {error_count} ERRORS in {len(errors_by_file)} files:")
        print()
        for fname, errs in sorted(errors_by_file.items()):
            print(f"  📄 {fname}")
            for e in errs:
                print(f"     • {e}")
            print()
    else:
        print(f"✅ All {total} recipes passed structural validation!")

    if dupes:
        sys.exit(1)
    if error_count > 0:
        sys.exit(1)

    print(f"\n✅ All checks passed for {total} recipes.")

if __name__ == "__main__":
    main()
