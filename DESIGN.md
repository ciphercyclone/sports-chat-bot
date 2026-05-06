---
name: Athletic Utility
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#41493e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#717a6d'
  outline-variant: '#c0c9bb'
  surface-tint: '#2a6b2c'
  primary: '#00450d'
  on-primary: '#ffffff'
  primary-container: '#1b5e20'
  on-primary-container: '#90d689'
  inverse-primary: '#91d78a'
  secondary: '#1b6d24'
  on-secondary: '#ffffff'
  secondary-container: '#a0f399'
  on-secondary-container: '#217128'
  tertiary: '#00460e'
  on-tertiary: '#ffffff'
  tertiary-container: '#006017'
  on-tertiary-container: '#7cdb7a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#acf4a4'
  primary-fixed-dim: '#91d78a'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#0c5216'
  secondary-fixed: '#a3f69c'
  secondary-fixed-dim: '#88d982'
  on-secondary-fixed: '#002204'
  on-secondary-fixed-variant: '#005312'
  tertiary-fixed: '#98f994'
  tertiary-fixed-dim: '#7ddc7a'
  on-tertiary-fixed: '#002204'
  on-tertiary-fixed-variant: '#005313'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-lg:
    fontFamily: Lexend
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-md:
    fontFamily: Lexend
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Lexend
    fontSize: 17px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Lexend
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.1px
  label-sm:
    fontFamily: Lexend
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.5px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  margin: 16px
  gutter: 12px
  touch-target: 44px
---

## Brand & Style

The design system is built for a high-performance, mobile-first sports experience. It balances the urgency of live sports with the conversational ease of a chatbot. The personality is authoritative yet approachable—functioning as a digital "coach" or "sideline reporter."

The visual style is a **Corporate / Modern** hybrid. It leverages the clarity and translucency of Apple’s Human Interface Guidelines to ensure content remains the focus, while adopting the structural rigor, tactile elevation, and functional component logic of Material Design 3. The result is a UI that feels disciplined, legible, and physically grounded.

## Colors

The palette is anchored by "Stadium Green," a deep, high-contrast primary color that evokes the turf of a pitch or field. This is paired with a neutral "Dark Charcoal" for typography to ensure maximum readability against light surfaces.

- **Primary:** Used for key actions, active states, and branding accents.
- **Surfaces:** A clean white is used for conversational bubbles and cards, while a light grey provides a soft, non-distracting backdrop for the chat stream.
- **Feedback:** Use standard semantic greens and reds for win/loss indicators, but keep them secondary to the brand green.

## Typography

The design system utilizes **Lexend** across all levels. This typeface was specifically designed to reduce visual stress and improve reading proficiency, making it ideal for the rapid-fire consumption of sports stats and chat messages.

- **Headlines:** Bold and rhythmic, used for scores and team names.
- **Body:** Set at 17px for primary chat bubbles to match mobile standard legibility.
- **Labels:** Used for metadata (timestamps, player positions) and MD3-style chip text.

## Layout & Spacing

This design system follows a **fluid grid** model optimized for narrow viewports. It employs an 8dp linear spacing scale, ensuring that all elements align to a consistent rhythmic baseline.

- **Margins:** A standard 16px lateral margin keeps content safe from screen edges.
- **Touch Targets:** All interactive elements (buttons, chips, icons) must maintain a minimum height and width of 44pt to accommodate athletic, high-speed interaction.
- **Chat Rhythm:** Use 8px spacing between messages from the same sender and 16px between different senders.

## Elevation & Depth

Hierarchy is established through a combination of **tonal layers** and **ambient shadows**. 

1. **Headers:** Use HIG-inspired background blur (System Ultra-Thin Material) with a subtle bottom shadow to remain fixed at the top of the chat, allowing messages to scroll underneath with a sense of depth.
2. **Surface Container:** The main chat background is flat (#F5F5F5).
3. **Chat Bubbles:** These sit on the "Surface" level with minimal elevation (1dp shadow) or no shadow at all, using color to differentiate between the user (Primary Green) and the bot (White).
4. **Interactive Cards:** Use MD3 Level 2 elevation (small, soft shadow) to indicate they are tappable and contain rich data like game summaries or player stats.

## Shapes

The shape language is friendly and modern. A consistent **Rounded (0.5rem)** corner radius is applied to standard components, while chat bubbles and chips utilize larger radii to feel more conversational.

- **Message Bubbles:** Use `rounded-xl` (1.5rem) on three corners, with the corner pointing to the sender being sharper.
- **Chips:** Fully pill-shaped (3rem) for a distinct "Material" feel.
- **Cards:** `rounded-lg` (1rem) to create a clear container for data.

## Components

### Chat Bubbles
- **User:** Stadium Green background, White text. Aligned right.
- **Bot:** White background, Dark Charcoal text. Aligned left. High corner radius (24px) for a soft, approachable feel.

### Outlined Chips
Following MD3 specs, chips should have a 1px border using the primary green or a light grey divider color. They are used for quick-reply suggestions (e.g., "See Stats," "Full Schedule").

### Elevated Headers
The header contains the bot's identity and navigation. It must use a 44pt height for touch targets and a backdrop blur effect to maintain context of the scrolling list.

### Buttons
Primary buttons are filled with Stadium Green. They must be at least 44pt high, utilizing the full width of the chat container minus margins for primary actions.

### Score Cards
Rich components used by the bot to display real-time data. These should be white, elevated, and contain internal padding of 16px, using Lexend Bold for the scores.

### Input Field
The persistent bottom bar should be white, separated by a light grey border, containing a text field with a 44pt height and an icon button for "Send" in the primary green.