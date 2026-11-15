# Jakester full-motion implementation brief — approved 2026-11-14

User explicitly rejected a static preview. Deliver an interactive animated Officer Jakester matching the supplied original full-body and punch-sequence artwork, not a still image, before asking for visual approval.

## Non-negotiable visual identity
Muscular anthropomorphic pig sheriff with short spiked dark hair, beard, reddish pig face, orange/black plaid rolled-sleeve shirt, tactical vest, gold sheriff badge, gloves, dark cargo pants, knee pads, holster and heavy boots. Match the user-supplied reference images closely. Avoid the current blocky placeholder.

## Animated moves and blends
- Locomotion: guarded idle, walk forward/back, crouch transition and crouch idle, jump takeoff/air/landing, dodge backstep and sidestep.
- Punches: left jab, right cross, right-hand heavy from arm appearing on viewer-left, sequential left-right combo, crouch punch, air punch. Six phases: guard, wind-up, drive, extension/impact, follow-through, recover. Maintain opposite hand protecting face throughout.
- Kicks: front kick, roundhouse, low crouch sweep, jumping kick.
- Defense: standing/crouching block, timed block-to-spinning-back-kick reversal with guard recovery.
- Grapples: grab, throw, opponent stagger, fall and get-up; requires articulated training opponent.
- Combat feedback: readable contact frames, grounded footwork, natural hips/torso/shoulder rotation, no arm stretching, distinct attack ranges, no frozen poses.

## Technical acceptance
Keep current v10 control build intact until animated candidate works. Build separately in a new branch or directory. Use a genuinely skinned/rigged 3D model (e.g. GLB) with animation clips/state machine and blended transitions, not a flat sprite pasted onto the old 2D figure. Optimize for iPhone Safari; test mobile inputs and animation rendering. Confirm animations visually before promoting to the main live Lab. Use free/open-source tools, no purchases. Preserve separate main Battle for Oinkaverse repository.

## Status
Specification only. No 3D mesh, rig, motion clips, or tested animated candidate produced by this document.
