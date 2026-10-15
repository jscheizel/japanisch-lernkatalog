/* Semantische Tags für die Satz-Engine (window.VOKABULAR_TAGS).
   Schlüssel = abgeleitete SRS-ID "v:<kana>|<lesson>" (siehe srs.js · srsId).
   subj3 = 3. Person Singular mit Artikel (für korrekte deutsche Verbform „Der Mann isst …").
   Erzeugt mit quellen/werkzeug/gen_tags.py — dort ändern, nicht hier. */
window.VOKABULAR_TAGS = {
  /* ---- Personen / Subjekte ---- */
  "v:おとこのひと|0": ["person", "subj3"],
  "v:おんなのひと|0": ["person", "subj3"],
  "v:こども|0": ["person", "subj3"],
  "v:おとこのこ|0": ["person", "subj3"],
  "v:おんなのこ|0": ["person", "subj3"],
  /* ---- Personen ---- */
  "v:わたし|0": ["person"],
  "v:あなた|0": ["person"],
  /* ---- Familie & Freunde (Begleiter mit と) ---- */
  "v:りょうしん|0": ["person", "family"],
  "v:ともだち|0": ["person", "family"],
  "v:かぞく|0": ["person", "family"],
  /* ---- Rollen/Berufe (Prädikatsnomen) ---- */
  "v:せんせい|0": ["role"],
  "v:かいしゃいん|2": ["role"],
  /* ---- Essen ---- */
  "v:すし|0": ["food"],
  "v:てんぷら|0": ["food"],
  "v:ラーメン|0": ["food"],
  "v:ピザ|0": ["food"],
  "v:ケーキ|0": ["food"],
  "v:パン|3": ["food"],
  "v:やさい|0": ["food"],
  "v:くだもの|5": ["food"],
  "v:さかな|0": ["food"],
  /* ---- Getränke ---- */
  "v:みず|0": ["drink"],
  "v:コーヒー|0": ["drink"],
  "v:ビール|0": ["drink"],
  "v:ワイン|3": ["drink"],
  "v:コーラ|1": ["drink"],
  "v:ミルク|8": ["drink"],
  /* ---- Lesbares ---- */
  "v:ほん|0": ["readable"],
  "v:しんぶん|0": ["readable"],
  "v:まんが|6": ["readable"],
  "v:ざっし|13": ["readable"],
  "v:てがみ|2": ["readable"],
  /* ---- Dinge ---- */
  "v:かばん|0": ["thing"],
  "v:ペン|0": ["thing"],
  "v:カメラ|1": ["thing"],
  "v:とけい|3": ["thing"],
  "v:かさ|5": ["thing"],
  "v:スマホ|5": ["thing"],
  /* ---- Orte ---- */
  "v:がっこう|0": ["place"],
  "v:だいがく|0": ["place"],
  "v:かいしゃ|0": ["place"],
  "v:えき|0": ["place"],
  "v:こうえん|0": ["place"],
  "v:スーパー|0": ["place"],
  "v:デパート|0": ["place"],
  "v:としょかん|0": ["place"],
  "v:びょういん|0": ["place"],
  "v:レストラン|0": ["place"],
  "v:ぎんこう|0": ["place"],
  /* ---- Verkehrsmittel ---- */
  "v:でんしゃ|0": ["transport"],
  "v:バス|0": ["transport"],
  "v:じてんしゃ|0": ["transport"],
  "v:ちかてつ|0": ["transport"],
  "v:タクシー|2": ["transport"],
  "v:しんかんせん|5": ["transport"],
  "v:ひこうき|7": ["transport"],
  /* ---- い-Adjektive (Eigenschaft von Dingen) ---- */
  "v:おおきい|0": ["i_adj"],
  "v:ちいさい|0": ["i_adj"],
  "v:あたらしい|0": ["i_adj"],
  "v:やすい|0": ["i_adj"],
  "v:あかい|6": ["i_adj"],
  "v:あおい|6": ["i_adj"],
  "v:しろい|10": ["i_adj"],
  "v:くろい|10": ["i_adj"],
  /* ---- な-Adjektive (passend zu Orten) ---- */
  "v:しずか|5": ["na_adj", "na_place"],
  "v:ゆうめい|0": ["na_adj", "na_place"],
  "v:べんり|9": ["na_adj", "na_place"],
};
