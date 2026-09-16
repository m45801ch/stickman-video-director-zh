<!-- readme:hero -->

<div align="center">

[**繁體中文**](README.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Português do Brasil](README.pt-BR.md)

# Stickman Video Director

### 把任何想法，變成一支真正「動起來」的一分鐘火柴人影片。

一個 Codex Skill，就能把你的文案變成經過確認的旁白、以畫面為先的導演提案，以及按時長生成的 Gemini Omni Flash 提示詞；旁白可選英文或台灣中文 Edge TTS。

![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827?style=flat-square)
![Gemini Omni Flash](https://img.shields.io/badge/Gemini-Omni%20Flash-6d28d9?style=flat-square)
![一分鐘影片](https://img.shields.io/badge/Video-≈60%20seconds-0066ff?style=flat-square)
![MIT License](https://img.shields.io/badge/License-MIT-16a34a?style=flat-square)

適合製作發布在 **YouTube Shorts、TikTok、Instagram Reels 和 YouTube** 上的知識解說、勵志故事、教育短片與快節奏視覺內容。

</div>

<!-- readme:demos -->

## 兩種高對比風格，一套統一的視覺語言

| 白底黑火柴人 | 黑底白火柴人 |
|:---:|:---:|
| <!-- demo:light:start --><a href="assets/readme/light-theme-demo.mp4"><img src="assets/readme/light-theme-demo.gif" alt="白底黑火柴人和高飽和強調色的動態效果示範" width="600"></a><!-- demo:light:end --> | <!-- demo:dark:start --><a href="assets/readme/dark-theme-demo.mp4"><img src="assets/readme/dark-theme-demo.gif" alt="黑底白火柴人和高飽和強調色的動態效果示範" width="600"></a><!-- demo:dark:end --> |
| 白色畫布 · 黑色人物 | 黑色畫布 · 白色人物 |

> 點擊任一動態預覽，即可開啟帶聲音的完整 10 秒影片。如果這種視覺風格也讓你有了創作靈感，歡迎替儲存庫點一個 Star，讓更多創作者發現它。

## 有文案，不等於已經有了影片

一個好想法仍然可能生成一段平淡的動畫：一個人物、一個背景，十秒鐘裡幾乎沒有新的視覺變化。真正導演完整的一分鐘，需要設計開場鉤子、控制解釋節奏、創造貼合內容的視覺隱喻、推動鏡頭、連接場景，並在多次獨立生成之間鎖定一致性。

**Stickman Video Director 會在你消耗生成額度之前，先完成這些製作層面的思考。**

<!-- readme:advantages -->

## 為什麼短影片創作者會需要這個 Skill

| 優勢 | 你會得到什麼 |
|---|---|
| **更強的故事結構** | 在保留核心含義的前提下，把原始材料重組成強開場、遞進解釋和結尾回扣。 |
| **真正的確認節點** | 先展示清晰可讀的完整導演提案，再生成最終模型提示詞；在修改成本最低的時候調整故事。 |
| **豐富且相關的動態畫面** | 每段規劃三個時間節拍，並加入視覺隱喻、環境變化、鏡頭運動、文字節點、人物互動、轉場、BGM 與音效。 |
| **完整的生產鎖定** | 在每條獨立提示詞中重複人物、線條粗細、配色、聲音、台詞、音訊、轉場和負面約束。 |
| **真正適配畫幅的導演方式** | 針對 `9:16`、`16:9` 或 `1:1` 重新設計構圖、鏡頭路徑和文字位置，而不是只替換一個比例標籤。 |
| **可控的視覺反差** | 支援白底黑火柴人、黑底白火柴人，以及最多三種高飽和強調色。 |
| **忠於原始材料** | 不隨意編造缺乏依據的事實、資料、引語或產品賣點。 |

不需要 API，也不依賴 MCP。安裝 Skill、呼叫它，然後在對話中完成整個製作流程即可。

<!-- readme:platforms -->

## 同一個想法，為不同螢幕重新構圖

| 比例 | 適合場景 | 導演重點 |
|---|---|---|
| `9:16` | YouTube Shorts、TikTok、Instagram Reels | 垂直縱深、醒目的中央輪廓、層疊式揭示、適合手機閱讀的文字 |
| `16:9` | YouTube 知識影片、教育內容、視覺隨筆 | 橫向調度、側向鏡頭運動、分割畫面對比、充足的負空間 |
| `1:1` | 社群平台資訊流、緊湊的產品故事 | 強中心構圖、放射式運動、清晰的邊緣留白 |

<!-- readme:workflow -->

## 貼上 → 選擇 → 確認 → 生成 → 拼接

1. **貼上**文案、筆記、文章，或只提供一個主題。
2. **選擇** `16:9`、`9:16` 或 `1:1`，再選擇淺色或深色主題。
3. **選擇配音**語言與聲音（預設英文；也可選擇 Edge TTS 台灣中文），再確認包含旁白、參考翻譯、畫面、鏡頭、轉場、BGM 和音效的詳細導演提案。
4. **生成**目前提案獲得核准後、與時長對應數量的獨立 Gemini Omni Flash 提示詞。
5. **拼接**預設六段約十秒的影片；也可以指定總時長或段落數，例如 120 秒對應 12 段。

畫幅、主題、旁白語言、場景結構、配色、聲音或基調都可以修改。發生全域變更時，Skill 會回到提案階段並重新請求確認。

<!-- readme:output -->

## 最終會得到什麼

- 面向創作者的英文標題、核心觀點、開場鉤子、基調、配色、聲音與音樂方向
- 與指定時長對應的選定語言旁白（預設一分鐘；英文預設約 130–150 字；台灣中文按自然語速與時長控制）
- 與提示詞數量對應的不同畫面場景，每兩到三秒出現一次明顯變化
- 精確的選定語言台詞與參考翻譯
- 按需求數量生成、帶時間節拍和負面約束的獨立 Gemini Omni Flash 提示詞（預設六條）
- 前後匹配的結尾與開場，讓片段之間更容易銜接
- BGM、音效、一致性和最終拼接建議
- 可選的 Edge TTS 台灣中文配音匯出指令（`zh-TW-HsiaoChenNeural`）
- 可執行的 Edge TTS 生成器，可從單一或分段旁白文字產生 MP3／SRT
- 可執行的 FFmpeg 組裝器，可拼接片段並混合旁白、BGM、SFX 輸出 MP4
- 支援按 `clip-01`／`vo-01` 編號自動對齊旁白，並合併完整 SRT 時間軸

<details>
<summary><strong>範例請求</strong></summary>

```text
Use $directing-stickman-videos to turn this copy into a one-minute English stickman video:

Gravity bends space and time so strongly around a black hole that even light cannot escape.
```

Skill 會先詢問缺少的畫幅和主題，然後展示完整導演提案供你確認，確認前不會生成最終模型提示詞。未指定時長時，預設使用六幕、約一分鐘。

</details>

<!-- readme:install -->

## 安裝

複製儲存庫：

```bash
git clone https://github.com/kaomei/stickman-video-director.git
cd stickman-video-director
```

把可安裝的 Skill 資料夾複製到 Codex skills 目錄：

```bash
cp -R skills/directing-stickman-videos "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重新啟動 Codex，讓 Skill 出現在可用清單中。然後呼叫它並貼上你的素材：

```text
$directing-stickman-videos
```

### 生成配音與最終影片

安裝 Edge TTS 與 FFmpeg（需同時提供 `ffmpeg` 和 `ffprobe`）：

```bash
python -m pip install edge-tts
```

先將 Phase A 核准後的旁白拆成 `narration/vo-01.txt`、`vo-02.txt` 等檔案，再生成對應的 MP3／SRT：

```bash
python skills/directing-stickman-videos/scripts/edge_tts_generate.py \
  --input narration \
  --output-dir audio/voice \
  --voice zh-TW-HsiaoChenNeural
```

影片片段放在 `clips/clip-01.mp4`、`clip-02.mp4` 等路徑後，可依編號自動對齊配音並輸出最終 MP4 與完整 SRT：

```bash
python skills/directing-stickman-videos/scripts/assemble_video.py \
  --videos clips \
  --voice-dir audio/voice \
  --bgm audio/bgm.mp3 \
  --sfx audio/sfx.mp3 \
  --output output/final.mp4
```

使用 `--dry-run` 可先預覽命令；工具會在配音與影片時長差異超過 0.25 秒時發出警告。

<!-- readme:reliability -->

## 為反覆修改而設計，也誠實面對生成差異

- **確認必須明確。** 目前提案沒有得到核准前，不會進入 Phase B。
- **全域變更會觸發重新構圖。** 新畫幅或新主題會重新設計導演提案，而不是機械替換文字。
- **提示詞可以獨立使用。** 每條都會重複獨立生成所需的關鍵鎖定條件。
- **內容始終有依據。** Skill 可以強化結構與表達，但不會添加沒有來源的主張。
- **音訊仍可能存在差異。** 獨立生成的影片可能出現輕微的聲音或音樂差異。追求最高一致性時，可以保留每段同步音效，並在拼接時使用一條連續的外部旁白和 BGM。

## 儲存庫結構

```text
skills/directing-stickman-videos/  可安裝的 Skill
assets/readme/                     README 示範素材
tests/                             行為情境與驗證腳本
docs/superpowers/specs/            已確認的產品設計
docs/superpowers/plans/            實作計畫
```

<!-- readme:contribute -->

## 一起把它做得更好

歡迎提交使用案例、提示詞改進、真實生成紀錄與具體建議。你可以建立 issue，或透過 pull request 提交範圍明確、能夠重現的變更。

如果這個 Skill 幫你把一個遲遲沒有完成的想法，變成了一支真正可以發布的影片，**請替儲存庫點一個 Star**。它會幫助下一個正在尋找相同工作流程的創作者發現這個專案。

## 授權條款

MIT
