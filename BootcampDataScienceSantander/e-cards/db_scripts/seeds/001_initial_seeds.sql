-- Seed collections
INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection) VALUES
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);

-- Seed types
INSERT INTO tbl_types (typeName) VALUES
('Fire'),
('Water'),
('Grass'),
('Electric'),
('Psychic'),
('Fighting'),
('Darkness'),
('Metal'),
('Dragon'),
('Colorless');

-- Seed stages
INSERT INTO tbl_stages (stageName) VALUES
('Basic'),
('Stage 1'),
('Stage 2'),
('VMAX'),
('VSTAR');

-- Seed cards
INSERT INTO tbl_cards (hp, name, info, attack, damage, weak, resis, retreat, cardNumberInCollection, collection_id, type_id, stage_id) VALUES
(120, 'Charizard', 'Flame Pokémon from Base Set', 'Fire Spin', '100', 'Water', NULL, '3', 4, 1, 1, 3),
(60, 'Pikachu', 'Electric Mouse Pokémon from Jungle', 'Thunder Jolt', '30', 'Fighting', 'Metal', '1', 27, 2, 4, 1),
(90, 'Lapras', 'Water Pokémon from Fossil', 'Water Gun', '30+', 'Electric', NULL, '2', 10, 3, 2, 1),
(70, 'Jigglypuff', 'Balloon Pokémon from Jungle', 'Lullaby', '0', 'Fighting', 'Psychic', '1', 54, 2, 10, 1),
(130, 'Gengar', 'Shadow Pokémon from Fossil', 'Nightmare', '30', 'Darkness', 'Fighting', '2', 5, 3, 5, 3);
