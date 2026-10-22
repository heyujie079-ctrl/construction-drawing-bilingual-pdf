# Layout and QA Rules

## Visual hierarchy

- Preserve the source drawing as the primary layer.
- Use blue `#0070C0` for English translations and inch labels unless a reference drawing establishes another color.
- Set English translation text approximately equal to the Chinese annotation height or up to 10% larger when space permits.
- Keep inch labels similar in size to the source mm dimension text.
- Maintain consistent font, color, capitalization, and spacing across pages.

## Placement hierarchy

Apply these priorities in order:

1. Never cover Chinese text, mm dimensions, dimension/extension lines, leaders, geometry, symbols, or title-block content.
2. Place each inch value beside its own mm value, normally directly above or below horizontal dimensions and immediately left or right of vertical dimensions.
3. Keep the visual gap small: normally 0.25-1.0 text heights and never more than about 1.5 text heights unless the drawing has no local space.
4. Place English below its Chinese callout when possible. If that area is occupied, use the nearest blank space while preserving the leader relationship.
5. Keep paired or repeated dimensions aligned consistently within the same view.

Do not place a group of inch values in a distant legend. The reader must be able to identify the corresponding mm value without tracing across the drawing.

## Collision handling

When space is tight, use this order:

1. Move the text within the nearest blank area.
2. Wrap or shorten the English while preserving technical meaning.
3. Split a long translation into two or three short lines.
4. Reduce the translation font slightly, but keep it readable.
5. Omit a non-essential inch conversion rather than cover source information.

Never solve crowding by rasterizing the entire drawing or erasing source annotations.

## Inch conversion

- Formula: `inches = millimetres / 25.4`.
- Round to a whole inch with decimal half-up rounding.
- Examples: `600 mm -> 24 inch`, `1000 mm -> 39 inch`, `1524 mm -> 60 inch`, `2000 mm -> 79 inch`.
- Do not trust inch labels already present in a reference drawing; recalculate them.
- Retain prefixes such as `R` or `D` only when converting that dimension is requested and the label remains technically unambiguous.

## Visual review checklist

Inspect every page at full-page scale and at enlarged scale around dense regions.

- English is legible and correctly associated with the Chinese source.
- Every inch label is adjacent to its matching mm value.
- No added text intersects source text, lines, arrows, or geometry.
- Long translations do not intrude into another view.
- Repeated labels use consistent wording and placement.
- Page count, page size, drawing borders, logos, and title blocks are unchanged.
- The final PDF opens successfully and representative English text can be extracted.

When the user supplies markup comments, fix the marked items and then audit the entire document for the same class of issue.
