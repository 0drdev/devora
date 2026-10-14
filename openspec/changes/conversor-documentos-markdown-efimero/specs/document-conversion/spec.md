# Spec Delta

## Purpose

Permite convertir documentos de usuario a Markdown fiel para reutilizarlos en modelos o agentes de IA, con formatos, límites y advertencias explícitos.

## ADDED Requirements

### Requirement: Ingesta con matriz de formatos explícita
The system SHALL accept only the documented format matrix and SHALL reject any other type with a clear error naming the supported formats.

#### Scenario: Archivo soportado es aceptado
- **WHEN** el usuario carga un PDF, DOCX, PPTX, XLSX, CSV, JSON, XML, HTML, TXT, MD, EPUB, ZIP, imagen o audio dentro de la matriz soportada
- **THEN** el sistema lo acepta para conversión y muestra su nombre, tipo y tamaño

#### Scenario: Tipo no soportado es rechazado
- **WHEN** el usuario carga un ejecutable u otro tipo fuera de la matriz
- **THEN** el sistema rechaza la carga y lista los formatos aceptados sin iniciar conversión

### Requirement: Conversión fiel a Markdown
The system SHALL produce Markdown that preserves headings hierarchy, lists, tables, links, and image alt-text or placeholders when present in the source.

#### Scenario: Documento ofimático conserva estructura
- **WHEN** se convierte un DOCX o PPTX con encabezados, listas, tablas y enlaces
- **THEN** el Markdown resultante conserva esa jerarquía y los enlaces como sintaxis Markdown

#### Scenario: Imagen incluye texto alternativo o marcador
- **WHEN** el documento contiene imágenes con descripción o texto extraíble
- **THEN** el Markdown incluye la descripción como alt-text o un marcador explícito cuando no hay texto

### Requirement: Límites y archivos inválidos
The system SHALL enforce configured size, page, and expansion limits and SHALL fail safely with a non-technical message for corrupt, password-protected, or oversized inputs.

#### Scenario: Archivo excede el límite
- **WHEN** el archivo supera el tamaño o páginas configurados
- **THEN** el sistema rechaza la conversión e indica el límite y cómo reducir el archivo

#### Scenario: Archivo protegido o corrupto
- **WHEN** el archivo está cifrado con contraseña o está corrupto
- **THEN** el sistema informa que no puede convertirse y no produce un Markdown parcial silencioso

### Requirement: Reporte de fidelidad sin pérdidas silenciosas
The system SHALL attach warnings for content that could not be converted faithfully and SHALL never silently drop pages, sheets, slides, or tables.

#### Scenario: Contenido parcialmente convertible
- **WHEN** una página, hoja, diapositiva o tabla no puede extraerse con fidelidad
- **THEN** el sistema entrega el Markdown disponible junto a una advertencia que identifica el elemento afectado

#### Scenario: Conversión completa sin advertencias
- **WHEN** todo el contenido se extrae con fidelidad
- **THEN** el sistema lo indica explícitamente para dar confianza en el resultado

### Requirement: Copia y descarga del resultado
The system SHALL offer copy-to-clipboard and download-as-`.md` for the generated Markdown, with confirmation of which action succeeded.

#### Scenario: Copiar y descargar
- **WHEN** la conversión termina y el usuario pulsa copiar o descargar
- **THEN** el sistema copia el Markdown al portapapeles o descarga un archivo `.md` con nombre derivado del original
