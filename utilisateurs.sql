DROP DATABASE IF EXISTS utilisateurs;

CREATE DATABASE utilisateurs;

USE utilisateurs;

CREATE TABLE utilisateur (
    id_utilisateur INT(3) NOT NULL AUTO_INCREMENT,
    nom VARCHAR(20) NOT NULL,
    empreinte VARCHAR(80),
    PRIMARY KEY (id_utilisateur)
) ENGINE = InnoDB;

INSERT INTO
    utilisateur
VALUES
    (
        '1',
        'roger',
        'bea45b0968d69663b7d656e573cf52f8408a781d15b3d255f7f76f5db3069d09'
    ),
    (
        '2',
        'bertrand',
        'f54dff746357502db7e8fa684e79f5f6ac063f65736077fe412e661a807cf43a'
    ),
    (
        '3',
        'pascal',
        'bc54f474d8df6ac3c2b597b4ac54a40ff75d60e25fc79f987510b594437de10b'
    ),
    (
        '4',
        'casimir',
        'eb5eeaf2a59ce928e047fa05a77c6e1c4db92bff13bf7cac0cd020119c8c6b2f'
    ),
    (
        '5',
        'JP',
        'be49d147d856bbe81e3719bf09b36a8352c2548b4c408d2b29b45b2a8fff0a0c'
    ),
    (
        '6',
        'manu',
        'e1826da2d3adb56bb822f882f1da16304ea6fcfbdaa8af7a1ffb91d412f338cd'
    ),
    (
        '7',
        'francoise',
        'beaaec19cf3d61a04127ad007b6f03a41d256bf924858a89441122cfd7d64f51'
    ),
    (
        '8',
        'etudiant',
        'f132b5aa31aaa78a33ee000e5c740fceec935f2655018e759477cd3d8fe2f90d'
    ),
    (
        '9',
        'test',
        '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    ),
    (
        '10',
        'admin',
        '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2'
    ),
    (
        '11',
        'root',
        '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
    );