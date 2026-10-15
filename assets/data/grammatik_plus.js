/* Erweiterte Grammatik (window.GRAMMATIK_PLUS) — Japanischkurs (Unterrichts-PDFs), Lektion 0–13.
   Erzeugt mit quellen/werkzeug/gen_grammatik.py — dort ändern, nicht hier.
   Schlüssel = exakter `pattern`-String aus grammatik.js.
   Felder je Eintrag (alle optional):
     erklaerung_lang : ausführliche Erklärung mit Nuancen
     fehler          : Liste häufiger Fehler
     kontrast        : Liste {a, b, note} — Abgrenzung verwandter Formen
     uebungen        : Liste von Übungen
                       { typ:"mc",    frage, optionen:[…], richtig:Index, erkl }
                       { typ:"cloze", satz (mit ＿), luecke:"…", erkl }
   Wird im Katalog additiv unter „Mehr erklären" angezeigt; Übungen laufen im Trainer mit. */
window.GRAMMATIK_PLUS = {
  "N1 は N2 です": {
    "erklaerung_lang": "は (geschrieben mit dem Hiragana は, gesprochen „wa“) nennt das Thema — das, worüber man spricht. です steht am Satzende und ändert sich nicht nach Person oder Zahl. Die Verneinung ist じゃありません (gesprochen) bzw. ではありません (förmlicher).",
    "fehler": [
      "は als Themenpartikel wird „wa“ gesprochen.",
      "Verneinung ist じゃありません, nicht „ですない“."
    ],
    "kontrast": [
      {
        "a": "は",
        "b": "が",
        "note": "は nennt das (bekannte) Thema, が hebt neue oder betonte Information hervor (z. B. bei あります/います, すき)."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "私＿学生です。",
        "optionen": [
          "は",
          "を",
          "へ",
          "で"
        ],
        "richtig": 0,
        "erkl": "は markiert das Thema „ich“."
      },
      {
        "typ": "cloze",
        "satz": "あの人は先生じゃ＿。（Verneinung）",
        "luecke": "ありません",
        "erkl": "じゃありません = „ist nicht“."
      }
    ]
  },
  "～か": {
    "erklaerung_lang": "Im Japanischen wird für eine Frage nichts umgestellt: Man hängt nur か an. Ein Fragezeichen ist nicht nötig, der Punkt 。 genügt. Fragewörter (なに, だれ, どこ …) stehen an der Stelle, an der in der Antwort die Information steht.",
    "fehler": [
      "Nicht die Wortstellung ändern — nur か anhängen."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "あなたは日本人です＿。",
        "optionen": [
          "か",
          "を",
          "に",
          "へ"
        ],
        "richtig": 0,
        "erkl": "か bildet die Frage."
      },
      {
        "typ": "cloze",
        "satz": "これは何です＿。",
        "luecke": "か",
        "erkl": "Frage → か am Satzende."
      }
    ]
  },
  "N1 の N2": {
    "erklaerung_lang": "Das Bestimmende steht immer vorn: 私の子ども (mein Kind), 日本語の本 (ein Japanischbuch), 大学の先生 (Lehrer an der Uni). Auch Ortsangaben werden so gebildet: つくえの上 = auf dem Schreibtisch.",
    "fehler": [
      "Reihenfolge nicht umdrehen: 私の車, nicht 車の私."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "私＿かばんです。",
        "optionen": [
          "の",
          "は",
          "を",
          "に"
        ],
        "richtig": 0,
        "erkl": "の zeigt die Zugehörigkeit („meine Tasche“)."
      },
      {
        "typ": "cloze",
        "satz": "つくえ＿上に本があります。",
        "luecke": "の",
        "erkl": "Ortsangaben: N の 上／下／中 …"
      }
    ]
  },
  "N が あります／います": {
    "erklaerung_lang": "Die Wahl hängt davon ab, ob sich das Ding von selbst bewegen kann: Menschen und Tiere → います, Gegenstände und Pflanzen → あります. Mit あります sagt man auch „haben“: じかんがあります = ich habe Zeit.",
    "fehler": [
      "Für Menschen und Tiere nicht あります benutzen.",
      "Das Vorhandene wird mit が markiert, nicht mit を."
    ],
    "kontrast": [
      {
        "a": "あります",
        "b": "います",
        "note": "あります = Dinge/Pflanzen, います = Menschen/Tiere."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "へやにねこが＿。",
        "optionen": [
          "います",
          "あります",
          "です",
          "します"
        ],
        "richtig": 0,
        "erkl": "Katze = Lebewesen → います."
      },
      {
        "typ": "mc",
        "frage": "つくえの上に本が＿。",
        "optionen": [
          "あります",
          "います",
          "いきます",
          "みます"
        ],
        "richtig": 0,
        "erkl": "Buch = Gegenstand → あります."
      }
    ]
  },
  "[Ort] に N が あります／います": {
    "erklaerung_lang": "Ortswörter sind im Japanischen Nomen: 上 (oben), 下 (unten), 中 (in), 前 (vor), うしろ (hinter), 右 (rechts), 左 (links), となり (neben), 間 (zwischen; A と B の 間). Sie hängen mit の am Bezugswort. Fragt man, wo etwas ist, dreht man um: 本はどこにありますか。…つくえの上にあります。",
    "fehler": [
      "Bezugswort + の + Ortswort: つくえの上 (nicht 上のつくえ).",
      "Ort mit に, nicht mit で (で ist für Handlungen)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "つくえの上＿本があります。",
        "optionen": [
          "に",
          "で",
          "を",
          "が"
        ],
        "richtig": 0,
        "erkl": "Ort des Vorhandenseins → に."
      },
      {
        "typ": "mc",
        "frage": "„Zwischen Berg und Berg“ heißt …",
        "optionen": [
          "山と山の間",
          "山の間と山",
          "間の山と山",
          "山と間の山"
        ],
        "richtig": 0,
        "erkl": "A と B の 間."
      },
      {
        "typ": "cloze",
        "satz": "木の＿に鳥がいます。（oben, auf）",
        "luecke": "上",
        "erkl": "上 = oben, auf."
      }
    ]
  },
  "N1 や N2 (など)": {
    "erklaerung_lang": "と zählt vollständig auf (A und B — sonst nichts), や nennt nur Beispiele (A, B und anderes). など am Ende betont, dass noch mehr dazugehört.",
    "kontrast": [
      {
        "a": "A と B",
        "b": "A や B",
        "note": "と = vollständige Aufzählung, や = beispielhafte Aufzählung."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "へやにソファ＿ランプがあります。（u. a.）",
        "optionen": [
          "や",
          "を",
          "で",
          "へ"
        ],
        "richtig": 0,
        "erkl": "や = beispielhafte Aufzählung."
      }
    ]
  },
  "N を V-ます": {
    "erklaerung_lang": "を wird „o“ gesprochen. Das Verb steht immer am Satzende; davor stehen Zeit, Ort und Objekt. Zeitangaben ohne Zahl (まい日, あした) brauchen keine Partikel.",
    "fehler": [
      "を wird „o“ gesprochen.",
      "Das Verb steht am Ende des Satzes."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "パン＿たべます。",
        "optionen": [
          "を",
          "に",
          "へ",
          "が"
        ],
        "richtig": 0,
        "erkl": "Objekt → を."
      },
      {
        "typ": "cloze",
        "satz": "テレビ＿みます。",
        "luecke": "を",
        "erkl": "Was man sieht → を."
      }
    ]
  },
  "[Ort] へ 行きます": {
    "erklaerung_lang": "Bei Bewegungsverben (いきます, きます, かえります) steht das Ziel mit へ oder に. へ betont die Richtung, に das Ziel — im Alltag sind beide richtig.",
    "fehler": [
      "へ wird „e“ gesprochen, nicht „he“."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "がっこう＿いきます。",
        "optionen": [
          "へ",
          "を",
          "で",
          "が"
        ],
        "richtig": 0,
        "erkl": "Richtung → へ (oder に)."
      }
    ]
  },
  "[Ort] で V": {
    "erklaerung_lang": "Merke: に (Ort des Seins: あります, います, すみます) und で (Ort des Tuns: たべます, かいます, はたらきます). すみます ist eine Ausnahme: ベルリンにすんでいます.",
    "kontrast": [
      {
        "a": "へやに います",
        "b": "へやで ねます",
        "note": "に = wo etwas ist, で = wo etwas getan wird."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "レストラン＿ばんごはんをたべます。",
        "optionen": [
          "で",
          "に",
          "を",
          "へ"
        ],
        "richtig": 0,
        "erkl": "Ort einer Handlung → で."
      },
      {
        "typ": "mc",
        "frage": "こうえん＿犬がいます。",
        "optionen": [
          "に",
          "で",
          "を",
          "と"
        ],
        "richtig": 0,
        "erkl": "Ort des Vorhandenseins → に."
      }
    ]
  },
  "[Person] と V": {
    "erklaerung_lang": "と kann auch zwei Nomen vollständig verbinden („A und B“): パンとコーヒー. Mit einer Person vor einem Verb heißt es „mit“. Allein: ひとりで.",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "かぞく＿りょこうします。",
        "optionen": [
          "と",
          "を",
          "が",
          "は"
        ],
        "richtig": 0,
        "erkl": "mit jemandem → と."
      }
    ]
  },
  "[Mittel] で V": {
    "erklaerung_lang": "Wer zu Fuß geht, sagt あるいて (ohne で). Die Frage nach dem Mittel lautet なんで (womit?).",
    "fehler": [
      "„Zu Fuß“ ist あるいて, nicht あるいてで."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "じてん車＿がっこうへいきます。",
        "optionen": [
          "で",
          "を",
          "に",
          "が"
        ],
        "richtig": 0,
        "erkl": "Verkehrsmittel → で."
      }
    ]
  },
  "V ます／ました": {
    "erklaerung_lang": "Alle Verben folgen demselben Muster: ます → ません → ました → ませんでした. Die Gegenwartsform drückt auch die Zukunft aus (あした行きます = ich gehe morgen).",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "Vergangenheit von たべます:",
        "optionen": [
          "たべました",
          "たべません",
          "たべませんでした",
          "たべましょう"
        ],
        "richtig": 0,
        "erkl": "ます → ました."
      },
      {
        "typ": "cloze",
        "satz": "きのう、テレビを見＿。（nicht gesehen）",
        "luecke": "ませんでした",
        "erkl": "verneinte Vergangenheit → ませんでした."
      }
    ]
  },
  "い-Adj. / な-Adj. + です": {
    "erklaerung_lang": "い-Adjektive enden auf い und werden selbst konjugiert (たかい → たかくない). な-Adjektive brauchen vor einem Nomen な (きれいな花) und werden über です verneint (きれいじゃありません). Achtung: きれい und ゆうめい sind な-Adjektive, obwohl sie auf い enden. いい wird zu よくない.",
    "fehler": [
      "きれい ist ein な-Adjektiv: きれいな花, nicht きれい花.",
      "いい → よくないです (nicht いくないです)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "Verneinung von たかいです:",
        "optionen": [
          "たかくないです",
          "たかいじゃありません",
          "たかくありませんでした",
          "たかいません"
        ],
        "richtig": 0,
        "erkl": "い-Adj.: い → くない."
      },
      {
        "typ": "mc",
        "frage": "きれい＿花",
        "optionen": [
          "な",
          "の",
          "い",
          "—"
        ],
        "richtig": 0,
        "erkl": "な-Adjektiv vor Nomen → な."
      }
    ]
  },
  "N が すき です": {
    "erklaerung_lang": "すき ist ein な-Adjektiv („beliebt“). Deshalb: すきな人 (Person, die man mag), すきじゃありません (mag nicht). Das Gemochte steht mit が, nicht mit を.",
    "fehler": [
      "Nicht を: ねこがすきです (nicht ねこをすきです)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "私はすし＿すきです。",
        "optionen": [
          "が",
          "を",
          "に",
          "で"
        ],
        "richtig": 0,
        "erkl": "Gemochtes → が."
      }
    ]
  },
  "N1 のほうが N2 より ～": {
    "erklaerung_lang": "Beim Vergleich von zwei Dingen fragt man mit どちら (welches von beiden). In der Antwort steht der Gewinner mit のほうが, das Verglichene mit より. より allein reicht auch: 日本はかんこくより大きいです.",
    "fehler": [
      "より steht nach dem Verglichenen, nicht nach dem Gewinner."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "日本＿ほうがかんこくより大きいです。",
        "optionen": [
          "の",
          "は",
          "が",
          "を"
        ],
        "richtig": 0,
        "erkl": "N の ほうが …"
      },
      {
        "typ": "cloze",
        "satz": "ちゅうごくは日本＿大きいです。（größer als Japan）",
        "luecke": "より",
        "erkl": "より = als."
      }
    ]
  },
  "N の 中で N が いちばん ～": {
    "erklaerung_lang": "Der Rahmen steht mit の中で (unter …) oder einfach mit で (in Japan: 日本で). Danach folgt das Gewinner-Nomen mit が und いちばん + Adjektiv.",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "くだものの中で、なに＿いちばんすきですか。",
        "optionen": [
          "が",
          "を",
          "は",
          "に"
        ],
        "richtig": 0,
        "erkl": "Fragewort + が bei いちばん."
      }
    ]
  },
  "なにも／どこへも／だれも + Verneinung": {
    "erklaerung_lang": "Das Verb muss verneint sein — anders als im Deutschen gibt es eine doppelte Verneinung: なにも + ません. Mit へ／に: どこへも, mit Lebewesen: だれも.",
    "fehler": [
      "Das Verb muss verneint sein: なにもたべません (nicht なにもたべます)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "デパートへいきました。でも、なにも＿。",
        "optionen": [
          "かいませんでした",
          "かいました",
          "かいます",
          "かいましょう"
        ],
        "richtig": 0,
        "erkl": "なにも + Verneinung."
      },
      {
        "typ": "cloze",
        "satz": "へやにだれ＿いません。",
        "luecke": "も",
        "erkl": "だれも + Verneinung = niemand."
      }
    ]
  },
  "～ませんか／～ましょう": {
    "erklaerung_lang": "Die verneinte Frage ませんか ist eine höfliche Einladung — die andere Person kann leicht absagen (ちょっと…). ましょう ist direkter: „Lass uns …“. Achtung: ましょうか (L4) bietet Hilfe an.",
    "kontrast": [
      {
        "a": "のみませんか",
        "b": "のみましょう",
        "note": "ませんか = Einladung (Frage), ましょう = Vorschlag/Zusage."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "いっしょにえいがを見＿。（Einladung）",
        "optionen": [
          "ませんか",
          "ましょうか",
          "ません",
          "ました"
        ],
        "richtig": 0,
        "erkl": "Einladung → ませんか."
      }
    ]
  },
  "～から、～": {
    "erklaerung_lang": "Im Japanischen steht der Grund vor der Folge: „teuer, weil — kaufe nicht“. Auf eine Frage mit どうして antwortet man mit ～から。. Das deutsche „deshalb“ entspricht derselben Struktur.",
    "fehler": [
      "Reihenfolge: Grund + から + Folge (nicht umgekehrt)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "さむいです＿、まどをしめます。",
        "optionen": [
          "から",
          "まで",
          "より",
          "が"
        ],
        "richtig": 0,
        "erkl": "Grund + から."
      },
      {
        "typ": "mc",
        "frage": "„Warum?“ heißt …",
        "optionen": [
          "どうして",
          "どこ",
          "いつ",
          "だれ"
        ],
        "richtig": 0,
        "erkl": "どうして = warum."
      }
    ]
  },
  "N1 に N2 を あげます／もらいます": {
    "erklaerung_lang": "Bei あげます steht der Empfänger mit に, bei もらいます der Geber mit に oder から. Gibt jemand MIR etwas, sagt man くれます: ともだちが私にプレゼントをくれました.",
    "kontrast": [
      {
        "a": "あげます",
        "b": "もらいます",
        "note": "あげます: ich → andere; もらいます: ich bekomme von anderen."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "ともだち＿プレゼントをあげました。",
        "optionen": [
          "に",
          "を",
          "で",
          "が"
        ],
        "richtig": 0,
        "erkl": "Empfänger → に."
      }
    ]
  },
  "Fragewörter": {
    "erklaerung_lang": "Fragewörter verbinden sich mit Partikeln: だれと (mit wem), どこで (wo — Handlung), どこへ (wohin), なんで (womit). Vor einem Fragewort als Subjekt steht が, nie は: だれがきましたか.",
    "fehler": [
      "Nach Fragewort als Subjekt が, nicht は: だれがいますか."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "＿日本へ行きますか。…らいねん行きます。",
        "optionen": [
          "いつ",
          "どこ",
          "だれ",
          "いくら"
        ],
        "richtig": 0,
        "erkl": "Zeit → いつ."
      },
      {
        "typ": "mc",
        "frage": "＿とえいがを見ましたか。…ともだちと。",
        "optionen": [
          "だれ",
          "なに",
          "どこ",
          "いつ"
        ],
        "richtig": 0,
        "erkl": "mit wem → だれと."
      }
    ]
  },
  "V たいです": {
    "erklaerung_lang": "～たい verhält sich wie ein い-Adjektiv: たい → たくない → たかった → たくなかった. Es beschreibt nur den eigenen Wunsch (oder den des Gesprächspartners in einer Frage). Das Objekt kann mit を oder が stehen: すしを／がたべたいです.",
    "fehler": [
      "Nicht für Dritte benutzen: „Er möchte …“ wird anders ausgedrückt.",
      "Verneinung: たくないです, nicht たいじゃありません."
    ],
    "kontrast": [
      {
        "a": "V-たいです",
        "b": "N が ほしいです",
        "note": "たい = etwas TUN wollen, ほしい = etwas HABEN wollen."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "すしを＿たいです。",
        "optionen": [
          "たべ",
          "たべます",
          "たべて",
          "たべる"
        ],
        "richtig": 0,
        "erkl": "ます-Stamm + たい."
      },
      {
        "typ": "mc",
        "frage": "Verneinung von 行きたいです:",
        "optionen": [
          "行きたくないです",
          "行きたいじゃありません",
          "行きませんたい",
          "行きたかったです"
        ],
        "richtig": 0,
        "erkl": "たい → たくない."
      },
      {
        "typ": "cloze",
        "satz": "子どもの時、ピアノをならい＿。（wollte）",
        "luecke": "たかったです",
        "erkl": "Vergangenheit: たかったです."
      }
    ]
  },
  "N が ほしいです": {
    "erklaerung_lang": "ほしい wird wie jedes い-Adjektiv konjugiert: ほしい → ほしくない → ほしかった → ほしくなかった. Wie bei すき steht das Gewünschte mit が. Für Handlungen nimmt man ～たい.",
    "fehler": [
      "Gewünschtes mit が, nicht を.",
      "Für Handlungen nicht ほしい, sondern ～たい."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "新しいかばん＿ほしいです。",
        "optionen": [
          "が",
          "を",
          "に",
          "で"
        ],
        "richtig": 0,
        "erkl": "Gewünschtes → が."
      },
      {
        "typ": "mc",
        "frage": "„Ich wollte keinen Hund.“",
        "optionen": [
          "犬はほしくなかったです",
          "犬がほしかったです",
          "犬がほしくないです",
          "犬をほしいです"
        ],
        "richtig": 0,
        "erkl": "verneinte Vergangenheit → ほしくなかったです."
      }
    ]
  },
  "子どもの 時、～": {
    "erklaerung_lang": "Die Zeit des Hauptsatzes richtet sich nach dem Satzende: 子どもの時、～ました. Weitere Beispiele: 休みの時 (in den Ferien), びょうきの時 (wenn man krank ist).",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "子ども＿時、ピアノをならいました。",
        "optionen": [
          "の",
          "は",
          "が",
          "に"
        ],
        "richtig": 0,
        "erkl": "N の 時."
      }
    ]
  },
  "Verbgruppen I / II / III": {
    "erklaerung_lang": "Faustregel: Steht vor ます ein Laut auf -e (たべ, あけ, しめ), ist es Gruppe II. Steht dort ein -i-Laut (のみ, かき, まち), ist es meistens Gruppe I — aber einige häufige Verben sind Ausnahmen und gehören zu Gruppe II: みます, ねます, おきます (aufstehen), います, あびます, かります, きます (anziehen). Gruppe III sind nur します (auch べんきょうします usw.) und きます (kommen).",
    "fehler": [
      "おきます (aufstehen) ist Gruppe II, おきます (hinlegen) ist Gruppe I — gleiche Kana, verschiedene Verben.",
      "みます und ねます sind Gruppe II, obwohl vor ます ein i-Laut steht."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "Zu welcher Gruppe gehört まちます?",
        "optionen": [
          "I",
          "II",
          "III"
        ],
        "richtig": 0,
        "erkl": "-i-ます, keine Ausnahme → Gruppe I."
      },
      {
        "typ": "mc",
        "frage": "Zu welcher Gruppe gehört みます?",
        "optionen": [
          "II",
          "I",
          "III"
        ],
        "richtig": 0,
        "erkl": "みます ist eine Ausnahme → Gruppe II."
      },
      {
        "typ": "mc",
        "frage": "Zu welcher Gruppe gehört そうじします?",
        "optionen": [
          "III",
          "I",
          "II"
        ],
        "richtig": 0,
        "erkl": "N + します → Gruppe III."
      }
    ]
  },
  "V て-Form": {
    "erklaerung_lang": "Merksatz für Gruppe I nach dem Laut vor ます: い・ち・り → って, み・び・に → んで, き → いて, ぎ → いで, し → して. Einzige Ausnahme: いきます → いって. Gruppe II ist einfach: ます durch て ersetzen. Gruppe III: して / きて.",
    "fehler": [
      "いきます → いって (nicht いいて).",
      "Gruppe-II-Verben nicht wie Gruppe I behandeln: みます → みて (nicht みって)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "て-Form von まちます:",
        "optionen": [
          "まって",
          "まちて",
          "まんで",
          "まいて"
        ],
        "richtig": 0,
        "erkl": "ち-ます → って."
      },
      {
        "typ": "mc",
        "frage": "て-Form von よみます:",
        "optionen": [
          "よんで",
          "よって",
          "よみて",
          "よいて"
        ],
        "richtig": 0,
        "erkl": "み-ます → んで."
      },
      {
        "typ": "mc",
        "frage": "て-Form von いきます:",
        "optionen": [
          "いって",
          "いいて",
          "いきて",
          "いんで"
        ],
        "richtig": 0,
        "erkl": "Ausnahme: いって."
      },
      {
        "typ": "cloze",
        "satz": "いそぎます → いそ＿",
        "luecke": "いで",
        "erkl": "ぎ-ます → いで."
      }
    ]
  },
  "N を ください": {
    "erklaerung_lang": "ください steht nach dem Objekt mit を. Mit すみません davor klingt es höflicher. Für Handlungen benutzt man die て-Form: ～てください.",
    "kontrast": [
      {
        "a": "N を ください",
        "b": "V-て ください",
        "note": "N を ください = etwas geben lassen; V-て ください = jemanden bitten, etwas zu tun."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "ビール＿ください。",
        "optionen": [
          "を",
          "が",
          "に",
          "で"
        ],
        "richtig": 0,
        "erkl": "N を ください."
      }
    ]
  },
  "V-て ください": {
    "erklaerung_lang": "～てください ist eine höfliche Bitte oder Anweisung. Mit すみません davor klingt es weicher. Die Verneinung („bitte nicht“) kommt in Lektion 13: ～ないでください.",
    "fehler": [
      "て-Form richtig bilden: まちます → まって (nicht まちて)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "でんきを＿ください。",
        "optionen": [
          "つけて",
          "つけます",
          "つける",
          "つけ"
        ],
        "richtig": 0,
        "erkl": "て-Form + ください."
      },
      {
        "typ": "cloze",
        "satz": "ちょっとまっ＿ください。",
        "luecke": "て",
        "erkl": "まちます → まって."
      },
      {
        "typ": "mc",
        "frage": "„Bitte helfen Sie mir!“",
        "optionen": [
          "てつだってください",
          "てつだいてください",
          "てつだってくださいか",
          "てつだいます"
        ],
        "richtig": 0,
        "erkl": "てつだいます → てつだって."
      }
    ]
  },
  "～から、V-て ください": {
    "erklaerung_lang": "Wie bei allen から-Sätzen steht der Grund vorn. Das Satzende (～てください) bestimmt, dass es eine Bitte ist.",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "あついです＿、エアコンをつけてください。",
        "optionen": [
          "から",
          "まで",
          "より",
          "や"
        ],
        "richtig": 0,
        "erkl": "Grund + から."
      }
    ]
  },
  "V-ましょうか": {
    "erklaerung_lang": "ましょうか ist ein Angebot (Soll ich …?). ましょう (ohne か) ist ein gemeinsamer Vorschlag (Lass uns …). Die Antwort auf ein Angebot ist oft ～てください oder お願いします.",
    "kontrast": [
      {
        "a": "もちましょうか",
        "b": "もってください",
        "note": "ましょうか = ich biete an; てください = ich bitte dich."
      },
      {
        "a": "いきましょう",
        "b": "いきましょうか",
        "note": "ましょう = Lass uns gehen; ましょうか = Sollen wir / soll ich gehen?"
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "„Soll ich das Fenster öffnen?“",
        "optionen": [
          "まどをあけましょうか",
          "まどをあけてください",
          "まどをあけたいです",
          "まどをあけませんか"
        ],
        "richtig": 0,
        "erkl": "Angebot → ましょうか."
      },
      {
        "typ": "cloze",
        "satz": "にもつをもち＿。…はい、お願いします。",
        "luecke": "ましょうか",
        "erkl": "Hilfe anbieten → ましょうか."
      }
    ]
  },
  "V-て います (Verlauf)": {
    "erklaerung_lang": "Die て-Form + います entspricht dem englischen -ing: Die Handlung ist im Gange. Verneinung: ～ていません, Vergangenheit: ～ていました (war gerade dabei).",
    "fehler": [
      "て-Form richtig bilden: よみます → よんでいます."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "今、テレビを＿います。",
        "optionen": [
          "見て",
          "見ます",
          "見",
          "見る"
        ],
        "richtig": 0,
        "erkl": "て-Form + います."
      },
      {
        "typ": "cloze",
        "satz": "やまださんは今、本をよん＿います。",
        "luecke": "で",
        "erkl": "よみます → よんで."
      }
    ]
  },
  "V-て います (Gewohnheit)": {
    "erklaerung_lang": "Mit Häufigkeitswörtern (まいにち, まいしゅう …) oder bei Berufen beschreibt ～ています einen andauernden Zustand des Lebens: „ich arbeite (zurzeit) bei …“. Frage nach dem Beruf: どこではたらいていますか。",
    "kontrast": [
      {
        "a": "今、はたらいています",
        "b": "ソニーではたらいています",
        "note": "Mit 今 = gerade jetzt; mit Firma/Häufigkeit = regelmäßig/beruflich."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "どこで＿いますか。…ソニーで。",
        "optionen": [
          "はたらいて",
          "はたらきて",
          "はたらいで",
          "はたらって"
        ],
        "richtig": 0,
        "erkl": "はたらきます → はたらいて."
      },
      {
        "typ": "mc",
        "frage": "„jeden Monat“ heißt …",
        "optionen": [
          "まいつき",
          "まいとし",
          "まいしゅう",
          "まいあさ"
        ],
        "richtig": 0,
        "erkl": "まいつき = jeden Monat."
      }
    ]
  },
  "V-て います (Zustand)": {
    "erklaerung_lang": "けっこんします heißt „heiraten“ (ein Moment), けっこんしています „verheiratet sein“ (Zustand). Genauso: すみます (sich niederlassen) → すんでいます (wohnen), もちます (in die Hand nehmen) → もっています (besitzen), かぜをひきます (sich erkälten) → ひいています (erkältet sein).",
    "fehler": [
      "„Ich bin verheiratet“ ist けっこんしています, nicht けっこんします."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "„Ich bin verheiratet.“",
        "optionen": [
          "けっこんしています",
          "けっこんします",
          "けっこんしました",
          "けっこんしたいです"
        ],
        "richtig": 0,
        "erkl": "Zustand → ～ています."
      },
      {
        "typ": "cloze",
        "satz": "私はベルリンにすん＿います。",
        "luecke": "で",
        "erkl": "すみます → すんで."
      }
    ]
  },
  "しって います／しりません": {
    "erklaerung_lang": "Eine Besonderheit: Die Bejahung lautet しっています, die Verneinung aber しりません. しっていません klingt falsch.",
    "fehler": [
      "Verneinung: しりません, nicht しっていません."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "あの人をしっていますか。…いいえ、＿。",
        "optionen": [
          "しりません",
          "しっていません",
          "しりませんでした",
          "しっています"
        ],
        "richtig": 0,
        "erkl": "Verneinung → しりません."
      }
    ]
  },
  "N を むかえに いきます／きます": {
    "erklaerung_lang": "Die abgeholte Person steht mit を, der Ort mit へ oder に. いきます = man geht hin, きます = jemand kommt zu mir.",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "えきへともだちを＿いきます。",
        "optionen": [
          "むかえに",
          "むかえて",
          "むかえ",
          "むかえを"
        ],
        "richtig": 0,
        "erkl": "むかえに いきます."
      }
    ]
  },
  "N を もって いきます／きます": {
    "erklaerung_lang": "Die Richtung entscheidet: von hier weg → もっていきます, zu mir her → もってきます. Beide werden wie いきます bzw. きます konjugiert.",
    "kontrast": [
      {
        "a": "もっていきます",
        "b": "もってきます",
        "note": "いきます = von mir weg (mitnehmen), きます = zu mir her (mitbringen)."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "„Bitte bring Wasser mit!“",
        "optionen": [
          "水をもってきてください",
          "水をもっていってください",
          "水をもちてください",
          "水をもってください"
        ],
        "richtig": 0,
        "erkl": "zu mir her → もってきます."
      }
    ]
  },
  "V1-て、V2-て、V3-ます": {
    "erklaerung_lang": "Die て-Form selbst hat keine Zeit. Erst das Verb am Ende sagt, ob es Gegenwart (ます), Vergangenheit (ました), Verneinung (ません), Bitte (てください) oder Wunsch (たいです) ist. Die Reihenfolge der Verben ist die Reihenfolge der Handlungen.",
    "fehler": [
      "Nicht jedes Verb in der Vergangenheit: おきて、行って、のみました (nur das letzte!)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "朝ごはんを＿、がっこうへ行きます。",
        "optionen": [
          "たべて",
          "たべます",
          "たべました",
          "たべたい"
        ],
        "richtig": 0,
        "erkl": "Verben in der Kette → て-Form."
      },
      {
        "typ": "mc",
        "frage": "„Ich bin aufgestanden und habe geduscht.“",
        "optionen": [
          "おきて、シャワーをあびました",
          "おきました、シャワーをあびて",
          "おきて、シャワーをあびて",
          "おきます、シャワーをあびました"
        ],
        "richtig": 0,
        "erkl": "Nur das letzte Verb trägt die Zeit."
      },
      {
        "typ": "cloze",
        "satz": "ローマへ行っ＿、ピザをたべたいです。",
        "luecke": "て",
        "erkl": "いきます → いって."
      }
    ]
  },
  "い-Adj. Vergangenheit": {
    "erklaerung_lang": "Die vier Formen: たかいです (ist teuer) · たかくないです (ist nicht teuer) · たかかったです (war teuer) · たかくなかったです (war nicht teuer). Ausnahme いい: よくないです, よかったです, よくなかったです.",
    "fehler": [
      "Nicht たかいでした — die Vergangenheit steckt im Adjektiv: たかかったです.",
      "いい → よかった (nicht いかった)."
    ],
    "kontrast": [
      {
        "a": "たかかったです",
        "b": "しずかでした",
        "note": "い-Adj.: Vergangenheit im Adjektiv; な-Adj.: Vergangenheit über でした."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "Vergangenheit von さむいです:",
        "optionen": [
          "さむかったです",
          "さむいでした",
          "さむくなかったです",
          "さむでした"
        ],
        "richtig": 0,
        "erkl": "い → かったです."
      },
      {
        "typ": "mc",
        "frage": "Vergangenheit von いいです:",
        "optionen": [
          "よかったです",
          "いかったです",
          "いいでした",
          "よくないです"
        ],
        "richtig": 0,
        "erkl": "Ausnahme: いい → よかった."
      },
      {
        "typ": "cloze",
        "satz": "ケーキはあま＿。（war nicht süß）",
        "luecke": "くなかったです",
        "erkl": "verneinte Vergangenheit: くなかったです."
      }
    ]
  },
  "な-Adj. Vergangenheit": {
    "erklaerung_lang": "Die vier Formen: しずかです · しずかじゃありません · しずかでした · しずかじゃありませんでした. Genauso bei Nomen: 学生でした (war Student). Achtung bei きれい, ゆうめい, しんせつ — sie sind な-Adjektive.",
    "fehler": [
      "きれい ist ein な-Adjektiv: きれいでした (nicht きれかったです)."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "Vergangenheit von べんりです:",
        "optionen": [
          "べんりでした",
          "べんりかったです",
          "べんりくなかったです",
          "べんりいでした"
        ],
        "richtig": 0,
        "erkl": "な-Adj. → でした."
      },
      {
        "typ": "mc",
        "frage": "„Die Stadt war nicht belebt.“",
        "optionen": [
          "まちはにぎやかじゃありませんでした",
          "まちはにぎやかくなかったです",
          "まちはにぎやかでした",
          "まちはにぎやかじゃありません"
        ],
        "richtig": 0,
        "erkl": "な-Adj. verneinte Vergangenheit."
      }
    ]
  },
  "N1 か N2": {
    "erklaerung_lang": "Am Satzende macht か eine Frage, zwischen zwei Nomen bedeutet es „oder“.",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "コーヒー＿おちゃをのみます。（oder）",
        "optionen": [
          "か",
          "と",
          "や",
          "も"
        ],
        "richtig": 0,
        "erkl": "か = oder."
      }
    ]
  },
  "い-Adj.-くて、～": {
    "erklaerung_lang": "Wie bei Verben trägt nur das letzte Glied die Zeit: あまくて、おいしかったです (war süß und lecker). Statt そして kann man so mehrere Eigenschaften in einem Satz nennen.",
    "fehler": [
      "いい → よくて (nicht いくて).",
      "Nur das letzte Adjektiv trägt die Vergangenheit."
    ],
    "kontrast": [
      {
        "a": "やすくて",
        "b": "しずかで",
        "note": "い-Adj. → くて, な-Adj./Nomen → で."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "このへやはひろ＿、あかるいです。",
        "optionen": [
          "くて",
          "で",
          "いで",
          "いくて"
        ],
        "richtig": 0,
        "erkl": "い-Adj. → くて."
      },
      {
        "typ": "mc",
        "frage": "„gut und billig“",
        "optionen": [
          "よくて、やすい",
          "いくて、やすい",
          "いいで、やすい",
          "よいで、やすい"
        ],
        "richtig": 0,
        "erkl": "いい → よくて."
      }
    ]
  },
  "な-Adj./N で、～": {
    "erklaerung_lang": "Die Formen lassen sich mischen: にぎやかで (な) + おもしろくて (い) + よかったです. Das Satzende bestimmt Zeit und Verneinung.",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "この町はしずか＿、きれいです。",
        "optionen": [
          "で",
          "くて",
          "な",
          "に"
        ],
        "richtig": 0,
        "erkl": "な-Adj. → で."
      },
      {
        "typ": "cloze",
        "satz": "ふじ山はゆうめい＿、きれいです。",
        "luecke": "で",
        "erkl": "ゆうめい ist ein な-Adjektiv → で."
      }
    ]
  },
  "V-て も いいです": {
    "erklaerung_lang": "Wörtlich: „Auch wenn ich … tue, ist es gut.“ Antwort bei Ja: はい、いいですよ／どうぞ. Bei Nein höflich: すみません、ちょっと… oder streng: いいえ、～てはいけません.",
    "fehler": [
      "て-Form richtig: すいます → すって, すわります → すわって."
    ],
    "kontrast": [
      {
        "a": "V-てもいいです",
        "b": "V-てはいけません",
        "note": "もいいです = dürfen, はいけません = nicht dürfen."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "ここでタバコをすって＿いいですか。",
        "optionen": [
          "も",
          "は",
          "を",
          "が"
        ],
        "richtig": 0,
        "erkl": "Erlaubnis → ても いいです."
      },
      {
        "typ": "mc",
        "frage": "„Darf ich hier sitzen?“",
        "optionen": [
          "ここにすわってもいいですか",
          "ここにすわってはいけません",
          "ここにすわってください",
          "ここにすわりましょうか"
        ],
        "richtig": 0,
        "erkl": "Erlaubnis fragen → てもいいですか."
      },
      {
        "typ": "cloze",
        "satz": "このでんわをつかっ＿もいいですか。",
        "luecke": "て",
        "erkl": "つかいます → つかって."
      }
    ]
  },
  "V-て は いけません": {
    "erklaerung_lang": "は wird hier „wa“ gesprochen. ～てはいけません ist ein klares, eher strenges Verbot (Schilder, Regeln). Höflicher bittet man mit ～ないでください (Lektion 13).",
    "fehler": [
      "は wird „wa“ gesprochen.",
      "Nicht ～てもいけません — Verbot ist ～ては いけません."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "ここでしゃしんをとって＿いけません。",
        "optionen": [
          "は",
          "も",
          "を",
          "が"
        ],
        "richtig": 0,
        "erkl": "Verbot → ては いけません."
      },
      {
        "typ": "mc",
        "frage": "„Du darfst den Hund nicht anfassen.“",
        "optionen": [
          "犬にさわってはいけません",
          "犬にさわってもいいです",
          "犬にさわってください",
          "犬にさわりたいです"
        ],
        "richtig": 0,
        "erkl": "Verbot → てはいけません."
      }
    ]
  },
  "ちょっと…": {
    "erklaerung_lang": "Ein direktes いいえ klingt im Japanischen oft unhöflich. Man sagt stattdessen すみません + ちょっと… und lässt den Satz offen; der Gesprächspartner versteht die Absage.",
    "uebungen": [
      {
        "typ": "mc",
        "frage": "Wie sagt man höflich ab?",
        "optionen": [
          "すみません、ちょっと…",
          "いいえ、いきません",
          "はい、いきましょう",
          "いいですよ"
        ],
        "richtig": 0,
        "erkl": "ちょっと… = höfliche Absage."
      }
    ]
  },
  "V ない-Form": {
    "erklaerung_lang": "Bei Gruppe I wird der i-Laut vor ます zum a-Laut: か(き)→か, の(み)→ま, ま(ち)→た. Endet der Stamm auf い, wird daraus わ (かいます → かわない, あいます → あわない). Gruppe II: einfach ます → ない. Gruppe III unregelmäßig: しない, こない.",
    "fehler": [
      "かいます → かわない (nicht かあない).",
      "きます (kommen) → こない (nicht きない).",
      "おきます (aufstehen, Gr. II) → おきない."
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "ない-Form von のみます:",
        "optionen": [
          "のまない",
          "のみない",
          "のんない",
          "のまらない"
        ],
        "richtig": 0,
        "erkl": "Gruppe I: み → ま."
      },
      {
        "typ": "mc",
        "frage": "ない-Form von かいます:",
        "optionen": [
          "かわない",
          "かあない",
          "かいない",
          "かない"
        ],
        "richtig": 0,
        "erkl": "い → わ."
      },
      {
        "typ": "mc",
        "frage": "ない-Form von きます (kommen):",
        "optionen": [
          "こない",
          "きない",
          "かない",
          "くない"
        ],
        "richtig": 0,
        "erkl": "Gruppe III: こない."
      },
      {
        "typ": "cloze",
        "satz": "たべます → たべ＿",
        "luecke": "ない",
        "erkl": "Gruppe II: ます → ない."
      }
    ]
  },
  "V-ないで ください": {
    "erklaerung_lang": "Gegenstück zu ～てください. Höflicher als ～てはいけません, weil es eine Bitte und kein Verbot ist. Mit から davor nennt man den Grund.",
    "kontrast": [
      {
        "a": "あけてください",
        "b": "あけないでください",
        "note": "てください = bitte tun, ないでください = bitte nicht tun."
      },
      {
        "a": "すわないでください",
        "b": "すってはいけません",
        "note": "ないでください = höfliche Bitte, てはいけません = Verbot."
      }
    ],
    "uebungen": [
      {
        "typ": "mc",
        "frage": "ここでしゃしんを＿ください。（bitte nicht）",
        "optionen": [
          "とらないで",
          "とって",
          "とらなくて",
          "とりないで"
        ],
        "richtig": 0,
        "erkl": "ない-Form + でください."
      },
      {
        "typ": "mc",
        "frage": "„Bitte vergiss deinen Schirm nicht!“",
        "optionen": [
          "かさをわすれないでください",
          "かさをわすれてください",
          "かさをわすれてはいけません",
          "かさをわすれませんか"
        ],
        "richtig": 0,
        "erkl": "negative Bitte → ないでください."
      },
      {
        "typ": "cloze",
        "satz": "まどをあけ＿ください。さむいですから。",
        "luecke": "ないで",
        "erkl": "Gr. II: あけない + でください."
      }
    ]
  },
};
