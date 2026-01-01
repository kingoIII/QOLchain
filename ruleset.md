D# Reglas base (ruleset) — QOLChain (borrador)

## Definiciones
- **Incidental / Ambiental**: sonido presente en el fondo de un registro sin intención deliberada de usar la obra como recurso principal.
- **Uso Comercial**: reproducción de la obra con intención de obtener beneficio económico directo (ej. vender el video, incluir en un anuncio, gran monetización del contenido).
- **Transformativo**: uso que genera una obra nueva significativamente distinta a la original.

## Reglas fundamentales
1. **Presunción de incidentalidad**: la presencia de una obra en el fondo se considera incidental salvo evidencia de edición o intención de uso dirigida a la obra.
2. **Umbral temporal**: evitar reglas rígidas de segundos; preferir evidencia de edición/intención (por ejemplo, corte que sincroniza con la canción, mezcla deliberada, uso en primer plano).
3. **Prueba de intención**: reclamaciones comerciales requieren:
   - Registro QOL del reclamante.
   - EvidenceURI con timestamps y metadatos.
   - Declaración de intención (contrato, facturación, comunicaciones).
4. **Licencias comerciales**:
   - Se realizan como `QOL-Subcall` on-chain con scope, duración y royalties.
5. **Samples / Scarcity**:
   - El creador puede limitar `n` licencias vendibles por sample (ej. max 5).
   - Cada venta genera un `QOL-Subcall` con transferencia parcial o temporal de derechos según términos.
6. **Remedios**:
   - Si la disputa favorece al creador: compensación económica y/o bloqueo futuro del asset en plataformas que respeten QOLChain.
   - Si la disputa favorece al reclamado (usuario): restitución de contenido y desestimación.
7. **Transparencia y auditoría**:
   - Todas las `QOL-Subcall` deben ser públicas y consultables.
8. **Excepciones**:
   - Uso educativo, cita crítica, y parodia pueden estar permitidos bajo condiciones de Transformative Use (documentadas en cada QOL).
9. **Disputa**:
   - Se inicia `QOL_DISPUTE` con evidencia. La resolución sigue panel descentralizado (3 miembros) + appeals on-chain.

## Nota final
Estas reglas buscan humanizar la aplicación de derechos. Son redactables y sujetas a revisión por la Fundación antes de convertirse en ley del protocolo.
