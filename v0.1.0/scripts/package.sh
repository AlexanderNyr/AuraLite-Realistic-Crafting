#!/bin/bash
# Copyright (c) 2026 AlexanderNyr
# Licensed under CC BY-NC-SA 4.0 — see LICENSE.txt
# Packages the recipes into 3 distribution formats: datapack, Fabric, Forge
set -e
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
SRC="$ROOT/src"
BUILD="$ROOT/build"
FORMATS="$ROOT/formats"
VERSION="0.1.0-beta"
NAME="AuraLite Realistic Crafting"
MODID="auralite_realistic_crafting"
FILEBASE="AuraLiteRealisticCrafting"

rm -rf "$BUILD" "$FORMATS"
mkdir -p "$BUILD" "$FORMATS"

# ============================================================
# 1) DATAPACK
# ============================================================
DP="$FORMATS/datapack"
mkdir -p "$DP/data/minecraft"
cp -r "$SRC/data/minecraft/recipes" "$DP/data/minecraft/"
cat > "$DP/pack.mcmeta" <<EOF
{
  "pack": {
    "pack_format": 15,
    "description": "§b$NAME §7v$VERSION §8- §f1247 realistic recipes for MC 1.20.1"
  }
}
EOF
cp "$ROOT/README.md"   "$DP/README.md"   2>/dev/null || true
cp "$ROOT/LICENSE.txt" "$DP/LICENSE.txt" 2>/dev/null || true
cp "$ROOT/pack.png"    "$DP/pack.png"    2>/dev/null || true
( cd "$DP" && zip -qr "$BUILD/$FILEBASE-datapack-$VERSION.zip" . )

# ============================================================
# 2) FABRIC MOD
# ============================================================
FB="$FORMATS/fabric"
mkdir -p "$FB/data/minecraft"
cp -r "$SRC/data/minecraft/recipes" "$FB/data/minecraft/"
cat > "$FB/pack.mcmeta" <<EOF
{
  "pack": {
    "pack_format": 15,
    "description": "$NAME (Fabric)"
  }
}
EOF
cat > "$FB/fabric.mod.json" <<EOF
{
  "schemaVersion": 1,
  "id": "$MODID",
  "version": "$VERSION",
  "name": "$NAME",
  "description": "Replaces 1247 vanilla recipes with more realistic ones.",
  "authors": ["AlexanderNyr"],
  "license": "CC-BY-NC-SA-4.0",
  "icon": "assets/$MODID/icon.png",
  "environment": "*",
  "depends": {
    "minecraft": ">=1.20",
    "fabricloader": ">=0.14.0"
  }
}
EOF
# A minimal manifest
mkdir -p "$FB/META-INF"
cat > "$FB/META-INF/MANIFEST.MF" <<EOF
Manifest-Version: 1.0
Created-By: $NAME Build Script
EOF
cp "$ROOT/LICENSE.txt" "$FB/LICENSE.txt" 2>/dev/null || true
cp "$ROOT/README.md"   "$FB/README.md"   2>/dev/null || true
cp "$ROOT/pack.png"    "$FB/pack.png"    2>/dev/null || true
mkdir -p "$FB/assets/$MODID"
cp "$ROOT/pack.png"    "$FB/assets/$MODID/icon.png" 2>/dev/null || true
( cd "$FB" && zip -qr "$BUILD/$FILEBASE-fabric-$VERSION.jar" . )

# ============================================================
# 3) FORGE MOD
# ============================================================
FG="$FORMATS/forge"
mkdir -p "$FG/data/minecraft"
cp -r "$SRC/data/minecraft/recipes" "$FG/data/minecraft/"
cat > "$FG/pack.mcmeta" <<EOF
{
  "pack": {
    "pack_format": 15,
    "description": "$NAME (Forge)",
    "forge:resource_pack_format": 15,
    "forge:data_pack_format": 15
  }
}
EOF
mkdir -p "$FG/META-INF"
cat > "$FG/META-INF/mods.toml" <<EOF
modLoader="lowcodefml"
loaderVersion="[47,)"
license="CC-BY-NC-SA-4.0"
issueTrackerURL=""

[[mods]]
modId="$MODID"
version="$VERSION"
displayName="$NAME"
authors="AlexanderNyr"
logoFile="icon.png"
credits="Copyright (c) 2026 AlexanderNyr"
description='''
Replaces 1247 vanilla recipes with more realistic ones.
Pure data-driven mod — no Java code, just JSON recipes.
Works on both client and server.
'''

[[dependencies.$MODID]]
modId="forge"
mandatory=true
versionRange="[47,)"
ordering="NONE"
side="BOTH"

[[dependencies.$MODID]]
modId="minecraft"
mandatory=true
versionRange="[1.20,1.21)"
ordering="NONE"
side="BOTH"
EOF
cat > "$FG/META-INF/MANIFEST.MF" <<EOF
Manifest-Version: 1.0
Created-By: $NAME Build Script
EOF
cp "$ROOT/LICENSE.txt" "$FG/LICENSE.txt" 2>/dev/null || true
cp "$ROOT/README.md"   "$FG/README.md"   2>/dev/null || true
cp "$ROOT/pack.png"    "$FG/pack.png"    2>/dev/null || true
cp "$ROOT/pack.png"    "$FG/icon.png"    2>/dev/null || true
( cd "$FG" && zip -qr "$BUILD/$FILEBASE-forge-$VERSION.jar" . )

echo ""
echo "=== BUILD RESULTS ==="
ls -lh "$BUILD/"
echo ""
echo "Recipe count: $(ls "$SRC/data/minecraft/recipes" | wc -l)"
