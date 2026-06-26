🚀 Data Analyst Portfolio: Business Intelligence & Analytics Engineering
Por: Jacobo Galindo Ortiz | Perfil Junior-Mid (Evolutivo)
🎯 Declaración de Perfil Ejecutivo
Analista de Datos orientado a Business Intelligence, Analytics Engineering y optimización de métricas de negocio. Especializado en el aseguramiento de la calidad de datos (Data Quality), automatización de procesos y traducción de análisis estadísticos en recomendaciones accionables
. Mi enfoque principal es tender puentes entre la complejidad técnica y los requerimientos de la C-Suite, comunicando hallazgos mediante estructuras de alto impacto (C➔F➔I) para maximizar el Revenue y la Eficiencia Operativa
.
🗺️ El Faro de Posicionamiento: Ruta del Portafolio Evolutivo
Este repositorio documenta mi maduración técnica a través de 8 proyectos maestros. Cada fase representa un ciclo de vida de datos completo
.
Fase
Proyecto
Herramientas
Estatus
Enfoque de Excelencia Operacional
01
Fundamentos de Negocio y Velocidad Operativa
Excel, Sheets, Git
CONCLUIDO
SDLC, Modelado Dimensional y Tratamiento de Outliers (IQR)
.
02
Núcleo Analítico Transaccional
SQL Server, T-SQL
Próximamente
Optimización de queries (CTEs) y KPIs financieros
.
03
Hibridación Relacional y Reportes Ad-hoc
SQL + Excel/Sheets
Próximamente
Conexión directa ODBC para reportes automatizados
.
...
...
...
...
...
📂 Proyecto 1: Fundamentos de Negocio y Velocidad Operativa (Finalizado)
Auditoría de 250,000 transacciones para optimización logística y comercial.
🛠️ Ecosistema Tecnológico y Metodología
Debido a restricciones de entorno, se implementó una Normalización Lógica mediante fórmulas avanzadas en un ecosistema híbrido
:
Google Sheets: Cálculos matriciales automatizados con ARRAYFORMULA y LEN para asegurar la integridad ante celdas vacías
.
Excel Online: Gestión de ambigüedad regional (USA vs. México) reconstruyendo fechas mediante funciones de texto (DATE, MID, LEFT, RIGHT)
.
Excel 2013: Optimización del rendimiento mediante Referencias Estructuradas y formatos de tabla (Ctrl + T) para procesar grandes volúmenes sin degradar la memoria RAM
.
🏗️ Arquitectura y Modelado (Star Schema)
Se migró de una "tabla plana" a un Esquema en Estrella para garantizar la integridad referencial y eliminar redundancias
:
Fact_Orders: 250k registros con métricas de Lead Time y Revenue.
Dim_Tables: Catálogos maestros de Productos e Inventario vinculados mediante llaves primarias (product_id)
.
📈 Hallazgos Críticos (Metodología C➔F➔I)
Etapa 1: Auditoría de Lead Time (E0 - E6)
Contexto (C): Revisión de la eficiencia en tiempos de entrega sobre el pipeline de órdenes del Q1
.
Hallazgo (F): Se identificó un sesgo a la derecha extremo con una Media de 3.88 días frente a una Mediana de 3 días. El método IQR estableció un Límite Superior de 7 días, detectando anomalías operativas de hasta 45 días (y un 1.02% de datos nulos en registro)
.
Implicación (I): La Bodega A concentra el 59.70% de los retrasos
. Se recomienda adoptar la Mediana como KPI oficial de éxito y auditar los procesos de despacho en la Bodega A para eliminar cuellos de botella en productos críticos como "Monitor 24" y "Teclado Mec"
.
Etapa 2: Desempeño de Ventas y Rentabilidad (E7 - E9)
Contexto (C): Evaluación del rendimiento regional y financiero del primer semestre de 2026
.
Hallazgo (F): El negocio generó un Revenue de $452.1M con un Margen Bruto (GPM) estable del 42.7%. No obstante, se detectó una dependencia crítica de las Bodegas A y B, que suman el 90% de las unidades vendidas, mientras la Bodega C solo aporta el 2.0% del ingreso
.
Implicación (I): Se recomienda una redistribución equitativa del stock para mitigar la variación en ventas de la Bodega A y potenciar la participación de la Bodega C, aprovechando que el coeficiente de variación por región se mantiene estable (~84%)
.
🛡️ Gobernanza de Datos y Buenas Prácticas
Este repositorio sigue estándares de Ingeniería Senior para asegurar la integridad y seguridad:
Arquitectura Modular: Organización en carpetas /data, /reports y /docs para escalabilidad
.
Blindaje de Datos: Uso estricto de .gitignore para bloquear archivos pesados (.xlsx, .csv), manteniendo la base de 250k registros segura en entorno local conforme a GDPR
.
Documentación Senior: Uso del estándar C➔F➔I para traducir métricas técnicas en valor financiero para la alta dirección.