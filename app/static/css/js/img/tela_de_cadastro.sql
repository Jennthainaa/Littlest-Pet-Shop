CREATE DATABASE tela_de_cadastro;
USE tela_de_cadastro;

CREATE TABLE usuarios (
    id INT AUO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    usuario VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
);

import tkinter as tk
from tkinter import 
    