# Spec Delta

## Purpose

Ofrece una interfaz web accesible, robusta y en español para cargar, convertir, revisar, copiar y descargar Markdown solo con teclado y lector de pantalla.

## ADDED Requirements

### Requirement: Flujo completo operable por teclado
The system SHALL let users complete upload, convert, review, copy, and download using keyboard alone with visible focus and logical order.

#### Scenario: Flujo solo con teclado
- **WHEN** un usuario navega con Tab, Enter y Escape sin mouse
- **THEN** puede cargar, convertir, revisar el resultado, copiarlo y descargarlo sin trampas de foco

### Requirement: Compatibilidad con lector de pantalla
The system SHALL expose labels, roles, and live status updates so screen-reader users perceive progress, success, warnings, and errors.

#### Scenario: Anuncio de progreso y resultado
- **WHEN** inicia y termina una conversión
- **THEN** el lector anuncia carga, progreso, éxito o error y la presencia de advertencias de fidelidad

### Requirement: Estados y errores comprensibles
The system SHALL show loading, success, and failure states in plain Spanish without leaking technical details or document content.

#### Scenario: Error explicado en lenguaje claro
- **WHEN** falla una conversión por tipo, tamaño o archivo dañado
- **THEN** el sistema explica la causa y el siguiente paso en español claro

### Requirement: Revisión, copia y descarga accesibles
The system SHALL present raw Markdown and a rendered preview with accessible copy and download actions and success confirmation.

#### Scenario: Revisar y reutilizar el resultado
- **WHEN** la conversión termina
- **THEN** el usuario puede leer el Markdown y la vista previa, copiarlo y descargar el `.md`, con confirmación de cada acción

### Requirement: Diseño legible y responsive
The system SHALL remain usable at 200% zoom and on mobile and desktop, with sufficient contrast, reduced-motion respect, and no loss of actions.

#### Scenario: Uso con zoom y en móvil
- **WHEN** se usa con zoom al 200%, movimiento reducido o pantalla pequeña
- **THEN** todos los controles siguen visibles y operables sin solapamientos
