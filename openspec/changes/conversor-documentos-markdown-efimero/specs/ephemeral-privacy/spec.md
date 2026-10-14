# Spec Delta

## Purpose

Garantiza que documentos y resultados sean efímeros y confidenciales, sin base de datos ni retención oculta, para que la herramienta sea un puente de conversión confiable.

## ADDED Requirements

### Requirement: Sin persistencia en base de datos
The system SHALL NOT store uploaded files, generated Markdown, or derived content in any database or durable storage.

#### Scenario: Conversión sin base de datos
- **WHEN** un usuario convierte un documento
- **THEN** ningún contenido del archivo ni del Markdown se escribe en una base de datos

#### Scenario: Auditoría de persistencia
- **WHEN** se revisa la configuración y el despliegue
- **THEN** no existe conexión a base de datos ni volumen persistente asociado al contenido

### Requirement: Retención temporal y purga determinista
The system SHALL keep content only in ephemeral memory or temp storage for the active session and SHALL purge it on download, discard, expiry, or session end.

#### Scenario: Purga al descartar
- **WHEN** el usuario pulsa descartar o cierra la sesión
- **THEN** el archivo y el Markdown dejan de estar disponibles y el almacenamiento temporal se libera

#### Scenario: Expiración automática
- **WHEN** transcurre el tiempo máximo de retención configurado sin actividad
- **THEN** el sistema purga el contenido y muestra que ya no está disponible

### Requirement: Sin telemetría de contenido
The system SHALL NOT log, cache, or transmit document bytes or Markdown to analytics, logs, or third parties; only anonymous operational metadata MAY be recorded.

#### Scenario: Revisión de registros
- **WHEN** se inspeccionan registros y métricas
- **THEN** no aparece texto del documento ni Markdown, solo metadatos como tipo, tamaño y éxito o fallo

### Requirement: Entrada sanitizada y conversión local mínima
The system SHALL sanitize untrusted inputs, restrict conversion to uploaded bytes, and SHALL NOT fetch remote URLs automatically for conversion.

#### Scenario: Carga con nombre o ZIP malicioso
- **WHEN** llega un nombre de archivo con rutas, un ZIP con expansión excesiva o contenido sospechoso
- **THEN** el sistema lo neutraliza o rechaza sin acceder a rutas fuera del área temporal

#### Scenario: Sin fetching remoto implícito
- **WHEN** el documento contiene enlaces o referencias remotas
- **THEN** el sistema no las descarga automáticamente y lo indica si afecta la fidelidad

### Requirement: Mensaje de privacidad verificable
The system SHALL display an explicit ephemeral-processing notice and SHALL confirm when content has been purged.

#### Scenario: Aviso y confirmación
- **WHEN** el usuario abre la herramienta y cuando se purga el contenido
- **THEN** ve que nada se guarda en base de datos, cuánto tiempo se retiene y la confirmación de purga
