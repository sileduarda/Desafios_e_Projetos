CREATE TABLE tbl_collections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    collectionSetName VARCHAR(80) NOT NULL,
    releaseDate DATE NOT NULL,
    totalCardsInCollection SMALLINT UNSIGNED NOT NULL
);

CREATE TABLE tbl_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    typeName VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE tbl_stages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stageName VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE tbl_cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hp SMALLINT UNSIGNED,
    name VARCHAR(60) NOT NULL,
    info TEXT,
    attack VARCHAR(80),
    damage VARCHAR(10),
    weak VARCHAR(20),
    resis VARCHAR(20),
    retreat VARCHAR(20),
    cardNumberInCollection SMALLINT UNSIGNED NOT NULL,
    collection_id INT NOT NULL,
    type_id INT NOT NULL,
    stage_id INT NOT NULL,
    FOREIGN KEY (collection_id) REFERENCES tbl_collections(id),
    FOREIGN KEY (type_id) REFERENCES tbl_types(id),
    FOREIGN KEY (stage_id) REFERENCES tbl_stages(id)
);
