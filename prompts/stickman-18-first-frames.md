# 《一條線，改變的起點》18 組首幀雙語生圖 Prompt（16:9 / Style 2B / 台華語案）

- 規格：180s / 18 clips / 16:9 / Style 2B Cinematic Story / 旁白 zh-TW-HsiaoChenNeural

## 畫風母鎖・Style 2B 電影故事風（本案專用，嚴禁改寫）
> 本案選定 Style 2B，此母鎖只適用 2B。Style 1 純白／純黑、Style 2A 科技棚各有獨立鎖定（見 skill `Style unity lock`），不可混用。孤立參考卡可用素背景，但前景渲染（等粗黑線＋平塗）與本鎖一致。
- 前景一律：乾淨2D向量卡通，等粗黑線＋平塗色塊，僅柔陰影。
- 背景一律：暖調電影感工業場景，柔體積光＋淺景深。
- 禁止：寫實、3D、頹廢質感、電路板紋理、可見文字數字、色碼。
- EN（逐字貼進每組英文）：`clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only`
- NEG（每組負約束必含）：`no grunge textures, no circuit board textures, no photorealistic rendering`
- 本案風格鎖定：@style-2b（Style 2B Cinematic Story，全案唯一，禁混入 Style 1 / Style 2A 詞彙如網格、玻璃 UI、純白／純黑畫布）

---


- 用法：圖 = 每段影片的首幀。先跑 C1 定版，C1 成圖當 character reference 餵給 C2-C18。
- 人物錨點每張逐字相同，不要改寫。中文供理解，貼圖以英文為主。

## 全片母鎖（每張英文內已展開）
- Character C1: `A minimalist 2D animated stick figure wearing a bright orange construction hard hat (smooth safety shell, no stickers) and a light sky blue t-shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation.`
- Character C2-C18: `The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation.` 雙人時第二位同設計，僅以計數器區分。
- Style: `clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only; 16:9 left-center-right staging`
- Palette（只用普通話）: `warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt, soft cyan glow`，C15/C18 可加 `warm amber light`。
- Negative: `no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes`

## 鏡位總表

| C | 景別 | 角度 | 影片運鏡（不進生圖） |
|---|---|---|---|
| C1 | 大遠景 Wide | 平視微俯 | 左→右橫移進場 |
| C2 | 中景 Medium | 側面 90° 平視 | 固定＋輕推 |
| C3 | 中景 | 側面平視 | 原地 push-in 5% |
| C4 | 中近景 MCU | 正面微仰 | 靜止呼吸感 |
| C5 | 中景 | 低角度仰 20° | 橫向 match cut |
| C6 | 中景 | 側面平視 | 影片 shake／圖用傾斜構圖代替 |
| C7 | 中景雙人 | 背側跟隨 | 沿線倒 tracking |
| C8 | 中近景 | 環繞起點 | 半環繞 orbit |
| C9 | 近景＋特寫切 | 正面平視 | 三連跳切 |
| C10 | 中景→全景 | 俯視 45° | 中景硬切全景 |
| C11 | 全景 | 高俯視 | 緩推 |
| C12 | 俯瞰 Top-down | 垂直 90° | 佈置對比停留 |
| C13 | 寬中景 | 側面平視 | 兩端橫移呼應 |
| C14 | 低角度中景 | 貼地仰角 | 切低角度固定 |
| C15 | 中景雙人 | 正面平視 | 停格＋暖光起 |
| C16 | 特寫→中景 | 手部特寫起 | 特寫拉回中景 |
| C17 | 中景跟隨 | 背側 tracking | 沿線前進 tracking |
| C18 | 全景拉遠 | 高角度俯 | 拉遠＋漸暗 |

---

## C1 首幀（主視覺鎖定，先跑這張）
檔名：`c1`

鏡位：大遠景 Wide，平視微俯。
中：晨間儀電維修區大廣角首幀，空廠房門口，大捲左框外一半，阿哲手扶捲，右側地板孔空著配青光，高窗暖白光加體積光，右側大留白。
EN：
```text
16:9 wide first frame, slightly high eye-level, empty electrical maintenance bay doorway, large control cable reel half outside left frame, hand on reel, floor penetration hole empty right with soft cyan glow, warm white sunlight from high windows with soft volumetric rays, background racks depth, clean negative space right, lateral composition. Character: A minimalist 2D animated stick figure wearing a bright orange construction hard hat (smooth safety shell, no stickers) and a light sky blue t-shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt, soft cyan glow. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C2 首幀
檔名：`c2`

鏡位：中景 Medium，側面 90° 平視。
中：捲落地中央，蹲姿起始，線頭在手指向孔，線微彎，孔緣青光反射，淺景深。
EN：
```text
16:9 side medium first frame, 90-degree side eye-level, cable reel grounded center, crouching start pose, cable end in hand pointing to floor hole with gentle curve, soft cyan rim light on hole edge, shallow depth of field, warm morning industrial light. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt, soft cyan glow. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C3 首幀
檔名：`c3`

鏡位：中景，側面平視。
中：手前伸送線姿，身體微轉，散線小亂，方向箭頭圖示，輕推進感。
EN：
```text
16:9 medium first frame, side eye-level, hands extended feeding pose, slight body turn, cables lightly messy on floor with icon-only direction arrow, slight push-in feel. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C4 首幀
檔名：`c4`

鏡位：中近景 MCU，正面微仰。
中：彎腰低點凍結將起身，靜止呼吸感。
EN：
```text
16:9 medium close-up first frame, slight low-angle front view, frozen at bent-low peak about to rise, static breathing camera feel. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C5 首幀
檔名：`c5`

鏡位：中景，低角度仰 20°。
中：扶腰站姿，手在腰，視線看地上線，背景稍冷，橫向構圖。
EN：
```text
16:9 medium first frame, 20-degree low-angle look-up, standing with hand on waist looking at floor cable, background slightly cooler gray, horizontal composition. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C6 首幀
檔名：`c6`

鏡位：中景，側面平視，傾斜構圖代替震動。
中：拉之前一刻，雙手抓線前傾，線繃直將卡，身體蓄力，無揚塵無踉蹌。
EN：
```text
16:9 medium tense first frame BEFORE release, side eye-level with slight Dutch tilt, both hands gripping cable leaning forward, line taut straight about to jam, body coiled, no stumble no dust yet. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C7 首幀
檔名：`c7`

鏡位：中景雙人，背側跟隨。
中：踉蹌恢復站穩，小林右框外半身手持計數器將進。
EN：
```text
16:9 two-figure medium first frame, back-side follow angle, recovering stance, second identical-style figure half outside right holding click counter about to enter. Characters: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation, two figures same design second distinguished only by counter. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C8 首幀
檔名：`c8`

鏡位：中近景，環繞起點。
中：雙手鬆開纏繞結，線鬆垂將輕送。
EN：
```text
16:9 medium close-up first frame, orbit start angle, hands releasing untangled knot, cable slack hanging about to feed gently. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt, soft cyan glow. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C9 首幀
檔名：`c9`

鏡位：近景，正面平視。
中：線尾在孔口，計數器舉到胸前將按未按。
EN：
```text
16:9 close-up first frame, front eye-level, cable tail at hole mouth, click counter raised to chest about to click. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt, soft cyan glow. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C10 首幀
檔名：`c10`

鏡位：中景，正面平視。
中：計數器舉高，兩人對看，皺眉前一刻。
EN：
```text
16:9 medium first frame, front eye-level, counter held high, two identical hard-hat figures facing, frown just forming. Characters: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C11 首幀
檔名：`c11`

鏡位：全景，高俯視。
中：散亂全景，兩人低頭，燈微冷。
EN：
```text
16:9 wide first frame, high-angle overhead, messy cables reel hole and two figures heads down, slightly cool light. Characters: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C12 首幀
檔名：`c12`

鏡位：俯瞰 Top-down，垂直 90°。
中：視線貼地，散線空地，雙手下垂將整理，佈置對比起點。
EN：
```text
16:9 top-down first frame, vertical 90-degree angle, gaze to floor, messy cables and empty space, hands down about to tidy. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C13 首幀
檔名：`c13`

鏡位：寬中景，側面平視。
中：放線架剛立好滾輪靜止，兩人分站左右，線鬆弛未送。
EN：
```text
16:9 wide-medium first frame, side eye-level, pay-off stand just erected rollers still, two figures split left-right, cable slack before sending. Characters: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C14 首幀
檔名：`c14`

鏡位：低角度中景，貼地仰角。
中：跪墊剛鋪下，人站著俯視將跪。
EN：
```text
16:9 low-angle medium first frame, ground-level look-up, kneel mat just laid, figure standing looking down about to kneel. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C15 首幀
檔名：`c15`

鏡位：中景雙人，正面平視。
中：穩定跪姿，同伴望來將問話，暖琥珀光。
EN：
```text
16:9 medium two-shot first frame, front eye-level, stable kneeling pose, companion looking over about to ask, warm amber light. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm amber light, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C16 首幀
檔名：`c16`

鏡位：手部特寫起，正面。
中：笑容殘留，手搭線上，線微緊將卡。
EN：
```text
16:9 first frame starting from hand close-up, front view, lingering smile pose, hand resting on cable, line slightly tightening. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C17 首幀
檔名：`c17`

鏡位：中景跟隨，背側 tracking 起點。
中：手放開線頭垂地，視線沿線看轉折。
EN：
```text
16:9 medium follow first frame, back-side tracking start, hand released cable end on floor, gaze along line toward bend. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm morning white sunlight, deep gray floor, bright orange hard hat, light sky blue shirt. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```

## C18 首幀
檔名：`c18`

鏡位：全景拉遠，高角度俯。
中：最後一段在孔前，坐姿側視將穿過，地面乾淨，漸暗前一刻。
EN：
```text
16:9 wide pull-back first frame, high-angle look-down, final segment before hole, sitting side view about to pass through, clean floor, pre-fade mood. Character: The same minimalist 2D animated stick figure in a bright orange hard hat and light sky blue shirt, with simple black stick limbs and shorts, hollow circular head, no facial features. Clean 2D vector cartoon style with uniform medium black outlines, flat cel fills, vibrant colors, smooth 2D animation. Palette: warm amber light, deep gray floor, bright orange hard hat, light sky blue shirt, soft cyan glow. Style: clean 2D vector cartoon foreground with uniform medium black outlines and flat cel fills, rich full-color cinematic industrial environment, warm color grade, soft volumetric lighting, shallow depth of field, soft shadows only. Negative constraints: no photorealistic human skin, no 3D humanoid CGI models, no chaotic line glitches, no grunge textures, no circuit board textures, no photorealistic rendering, no extra limbs, no changed proportions, no broken line weight, no speech bubbles, no dialogue boxes, no visible words letters numbers captions subtitles logos watermarks, no hex RGB Pantone color codes.
```
