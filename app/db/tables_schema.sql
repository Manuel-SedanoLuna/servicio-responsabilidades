-- Active: 1727721349758@@127.0.0.1@32716@TPJ24833

CREATE TABLE PSU (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    folio VARCHAR(10),
    fecha DATE,
    hora VARCHAR(255),
    cr_plaza VARCHAR(10),
    pregunta_meta VARCHAR(2),
    plaza VARCHAR(255),
    tienda VARCHAR(20),
    encuesta VARCHAR(25),
    pregunta VARCHAR(255),
    respuesta VARCHAR(255),
    hallazgo_pregunta VARCHAR(255),
    numeracion VARCHAR(10),
    driver VARCHAR(50),
    seccion VARCHAR(50),
    region VARCHAR(50),
    zona VARCHAR(50),
    concepto VARCHAR(255),
    resp_op_id INT,
    FOREIGN KEY (resp_op_id) REFERENCES AMEF_GPT(id)
);


CREATE TABLE AMEF_GPT (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    seccion VARCHAR(255),
    responsabilidad_operativa VARCHAR(255),
    problematica VARCHAR(255),
    efecto_de_falla VARCHAR(255),
    severidad INT,
    ocurrencia INT,
    deteccion INT,
    riesgo_potencial INT,
    acciones_preventivas VARCHAR(255)
);


CREATE TABLE MODEL_INFO  (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    version VARCHAR(255),
    descripcion VARCHAR(255),
    fecha DATE 
);



CREATE TABLE SCORE_RESULTADOS (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    modelo_id INT,
    resp_op_id INT,
    seccion VARCHAR(255),
    problematica VARCHAR(255),
    efecto_falla VARCHAR(255),
    seccion VARCHAR(255),
    score DECIMAL(17, 16),
    tienda VARCHAR(255),
    is_activo BOOLEAN,
    fecha DATE,
    FOREIGN KEY (modelo_id) REFERENCES MODEL_INFO(id)
    FOREIGN KEY (resp_op_id) REFERENCES AMEF_GPT(id)
)
