# Grammatik je Lektion. Felder wie grammatik.js; zusätzlich je Punkt:
#   extra  = zusätzliche Beispielsätze (→ grammatik_extra.js)
#   plus   = erklaerung_lang / fehler / kontrast / uebungen (→ grammatik_plus.js)
# Beispielsätze sind an die Sätze der Unterrichts-PDFs angelehnt.
def B(jp, r, de): return {'jp': jp, 'r': r, 'de': de}
def MC(frage, optionen, richtig, erkl): return {'typ': 'mc', 'frage': frage, 'optionen': optionen, 'richtig': richtig, 'erkl': erkl}
def CL(satz, luecke, erkl): return {'typ': 'cloze', 'satz': satz, 'luecke': luecke, 'erkl': erkl}

G = []
def g(lesson, pattern, title, bildung, erklaerung, beispiele, extra=(), lang='', fehler=(), kontrast=(), uebungen=()):
    G.append(dict(lesson=lesson, pattern=pattern, title=title, bildung=bildung, erklaerung=erklaerung,
                  beispiele=list(beispiele), extra=list(extra),
                  plus={k: v for k, v in (('erklaerung_lang', lang), ('fehler', list(fehler)), ('kontrast', list(kontrast)), ('uebungen', list(uebungen))) if v}))

# ======================= Lektion 0 — vorausgesetzt =======================
g(0, "N1 は N2 です", "Aussagesatz (A ist B)",
  "N1 + は (wa) + N2 + です。 Verneinung: N1 は N2 じゃ／ではありません。",
  "は markiert das Thema des Satzes; です ist die höfliche Kopula („ist/sind“).",
  [B("私は学生です。", "Watashi wa gakusei desu.", "Ich bin Student(in)."),
   B("あの人は先生じゃありません。", "Ano hito wa sensei ja arimasen.", "Diese Person ist kein(e) Lehrer(in).")],
  extra=[B("山田さんは日本人です。", "Yamada-san wa nihonjin desu.", "Herr/Frau Yamada ist Japaner(in).")],
  lang="は (geschrieben mit dem Hiragana は, gesprochen „wa“) nennt das Thema — das, worüber man spricht. です steht am Satzende und ändert sich nicht nach Person oder Zahl. Die Verneinung ist じゃありません (gesprochen) bzw. ではありません (förmlicher).",
  fehler=["は als Themenpartikel wird „wa“ gesprochen.", "Verneinung ist じゃありません, nicht „ですない“."],
  kontrast=[{'a': 'は', 'b': 'が', 'note': 'は nennt das (bekannte) Thema, が hebt neue oder betonte Information hervor (z. B. bei あります/います, すき).'}],
  uebungen=[MC("私＿学生です。", ["は", "を", "へ", "で"], 0, "は markiert das Thema „ich“."),
            CL("あの人は先生じゃ＿。（Verneinung）", "ありません", "じゃありません = „ist nicht“.")])

g(0, "～か", "Fragesatz",
  "Aussagesatz + か。 Antwort: はい、～です。／いいえ、～じゃありません。",
  "か am Satzende macht aus einer Aussage eine Frage; die Wortstellung bleibt gleich.",
  [B("あなたは学生ですか。", "Anata wa gakusei desu ka.", "Bist du Student(in)?"),
   B("はい、学生です。", "Hai, gakusei desu.", "Ja, ich bin Student(in).")],
  extra=[B("あの人はドイツ人ですか。…いいえ、アメリカ人です。", "Ano hito wa doitsujin desu ka. … Iie, amerikajin desu.", "Ist diese Person Deutsche(r)? … Nein, Amerikaner(in).")],
  lang="Im Japanischen wird für eine Frage nichts umgestellt: Man hängt nur か an. Ein Fragezeichen ist nicht nötig, der Punkt 。 genügt. Fragewörter (なに, だれ, どこ …) stehen an der Stelle, an der in der Antwort die Information steht.",
  fehler=["Nicht die Wortstellung ändern — nur か anhängen."],
  uebungen=[MC("あなたは日本人です＿。", ["か", "を", "に", "へ"], 0, "か bildet die Frage."),
            CL("これは何です＿。", "か", "Frage → か am Satzende.")])

g(0, "N1 の N2", "Zugehörigkeit (の)",
  "N1 + の + N2 — N1 bestimmt N2 näher („von“, „aus“, „für“).",
  "の verbindet zwei Nomen: 私の車 = mein Auto, 日本の車 = ein Auto aus Japan.",
  [B("これは私の車です。", "Kore wa watashi no kuruma desu.", "Das ist mein Auto."),
   B("先生の本はあそこにあります。", "Sensei no hon wa asoko ni arimasu.", "Das Buch des Lehrers ist dort drüben.")],
  lang="Das Bestimmende steht immer vorn: 私の子ども (mein Kind), 日本語の本 (ein Japanischbuch), 大学の先生 (Lehrer an der Uni). Auch Ortsangaben werden so gebildet: つくえの上 = auf dem Schreibtisch.",
  fehler=["Reihenfolge nicht umdrehen: 私の車, nicht 車の私."],
  uebungen=[MC("私＿かばんです。", ["の", "は", "を", "に"], 0, "の zeigt die Zugehörigkeit („meine Tasche“)."),
            CL("つくえ＿上に本があります。", "の", "Ortsangaben: N の 上／下／中 …")])

g(0, "N が あります／います", "es gibt / haben",
  "N が あります (Dinge, Pflanzen) ／ N が います (Menschen, Tiere).",
  "あります für Unbelebtes, います für Lebewesen. Verneinung: ありません／いません.",
  [B("私の部屋にベッドがあります。", "Watashi no heya ni beddo ga arimasu.", "In meinem Zimmer gibt es ein Bett."),
   B("こうえんに犬がいます。", "Kōen ni inu ga imasu.", "Im Park ist ein Hund.")],
  extra=[B("お金がありません。", "Okane ga arimasen.", "Ich habe kein Geld.")],
  lang="Die Wahl hängt davon ab, ob sich das Ding von selbst bewegen kann: Menschen und Tiere → います, Gegenstände und Pflanzen → あります. Mit あります sagt man auch „haben“: じかんがあります = ich habe Zeit.",
  fehler=["Für Menschen und Tiere nicht あります benutzen.", "Das Vorhandene wird mit が markiert, nicht mit を."],
  kontrast=[{'a': 'あります', 'b': 'います', 'note': 'あります = Dinge/Pflanzen, います = Menschen/Tiere.'}],
  uebungen=[MC("へやにねこが＿。", ["います", "あります", "です", "します"], 0, "Katze = Lebewesen → います."),
            MC("つくえの上に本が＿。", ["あります", "います", "いきます", "みます"], 0, "Buch = Gegenstand → あります.")])

g(0, "[Ort] に N が あります／います", "Ortsangaben (上・下・中・前 …)",
  "[N の 上／下／中／前／うしろ／右／左／となり／間] に + N が あります／います。",
  "Positionswörter stehen nach の; der Ort wird mit に markiert.",
  [B("つくえの上にペンがあります。", "Tsukue no ue ni pen ga arimasu.", "Auf dem Schreibtisch liegt ein Stift."),
   B("木の下に子どもがいます。", "Ki no shita ni kodomo ga imasu.", "Unter dem Baum ist ein Kind."),
   B("山と山の間に川があります。", "Yama to yama no aida ni kawa ga arimasu.", "Zwischen den Bergen gibt es einen Fluss.")],
  extra=[B("いすはつくえの前にあります。", "Isu wa tsukue no mae ni arimasu.", "Der Stuhl steht vor dem Schreibtisch.")],
  lang="Ortswörter sind im Japanischen Nomen: 上 (oben), 下 (unten), 中 (in), 前 (vor), うしろ (hinter), 右 (rechts), 左 (links), となり (neben), 間 (zwischen; A と B の 間). Sie hängen mit の am Bezugswort. Fragt man, wo etwas ist, dreht man um: 本はどこにありますか。…つくえの上にあります。",
  fehler=["Bezugswort + の + Ortswort: つくえの上 (nicht 上のつくえ).", "Ort mit に, nicht mit で (で ist für Handlungen)."],
  uebungen=[MC("つくえの上＿本があります。", ["に", "で", "を", "が"], 0, "Ort des Vorhandenseins → に."),
            MC("„Zwischen Berg und Berg“ heißt …", ["山と山の間", "山の間と山", "間の山と山", "山と間の山"], 0, "A と B の 間."),
            CL("木の＿に鳥がいます。（oben, auf）", "上", "上 = oben, auf.")])

g(0, "N1 や N2 (など)", "Aufzählung (und … usw.)",
  "N1 や N2 (や N3) (など)",
  "や zählt beispielhaft auf („unter anderem“); など = „und so weiter“.",
  [B("私の部屋につくえやいすやベッドがあります。", "Watashi no heya ni tsukue ya isu ya beddo ga arimasu.", "In meinem Zimmer gibt es (u. a.) einen Schreibtisch, einen Stuhl und ein Bett."),
   B("コンビニでコーラやケーキなどをかいました。", "Konbini de kōra ya kēki nado o kaimashita.", "Im Konbini habe ich Cola, Kuchen und so weiter gekauft.")],
  lang="と zählt vollständig auf (A und B — sonst nichts), や nennt nur Beispiele (A, B und anderes). など am Ende betont, dass noch mehr dazugehört.",
  kontrast=[{'a': 'A と B', 'b': 'A や B', 'note': 'と = vollständige Aufzählung, や = beispielhafte Aufzählung.'}],
  uebungen=[MC("へやにソファ＿ランプがあります。（u. a.）", ["や", "を", "で", "へ"], 0, "や = beispielhafte Aufzählung.")])

g(0, "N を V-ます", "Objekt (を)",
  "N + を (o) + Verb.",
  "を markiert das direkte Objekt einer Handlung (was gegessen, gelesen, gekauft … wird).",
  [B("私はまい日コーヒーをのみます。", "Watashi wa mainichi kōhī o nomimasu.", "Ich trinke jeden Tag Kaffee."),
   B("ともだちと日本語をべんきょうします。", "Tomodachi to nihongo o benkyō shimasu.", "Ich lerne mit Freunden Japanisch.")],
  lang="を wird „o“ gesprochen. Das Verb steht immer am Satzende; davor stehen Zeit, Ort und Objekt. Zeitangaben ohne Zahl (まい日, あした) brauchen keine Partikel.",
  fehler=["を wird „o“ gesprochen.", "Das Verb steht am Ende des Satzes."],
  uebungen=[MC("パン＿たべます。", ["を", "に", "へ", "が"], 0, "Objekt → を."),
            CL("テレビ＿みます。", "を", "Was man sieht → を.")])

g(0, "[Ort] へ 行きます", "Richtung (へ / に)",
  "[Ort] へ (e) ／ に + 行きます／来ます／帰ります。",
  "へ (gesprochen „e“) gibt die Richtung einer Bewegung an.",
  [B("あした、日本へ行きます。", "Ashita, Nihon e ikimasu.", "Morgen fahre ich nach Japan."),
   B("私は七じにうちへかえります。", "Watashi wa shichi-ji ni uchi e kaerimasu.", "Ich gehe um sieben Uhr nach Hause.")],
  lang="Bei Bewegungsverben (いきます, きます, かえります) steht das Ziel mit へ oder に. へ betont die Richtung, に das Ziel — im Alltag sind beide richtig.",
  fehler=["へ wird „e“ gesprochen, nicht „he“."],
  uebungen=[MC("がっこう＿いきます。", ["へ", "を", "で", "が"], 0, "Richtung → へ (oder に).")])

g(0, "[Ort] で V", "Ort der Handlung (で)",
  "[Ort] + で + Verb (Handlung).",
  "で markiert den Ort, an dem etwas getan wird.",
  [B("スーパーでやさいをかいます。", "Sūpā de yasai o kaimasu.", "Ich kaufe im Supermarkt Gemüse."),
   B("としょかんで本をよみます。", "Toshokan de hon o yomimasu.", "Ich lese in der Bibliothek ein Buch.")],
  lang="Merke: に (Ort des Seins: あります, います, すみます) und で (Ort des Tuns: たべます, かいます, はたらきます). すみます ist eine Ausnahme: ベルリンにすんでいます.",
  kontrast=[{'a': 'へやに います', 'b': 'へやで ねます', 'note': 'に = wo etwas ist, で = wo etwas getan wird.'}],
  uebungen=[MC("レストラン＿ばんごはんをたべます。", ["で", "に", "を", "へ"], 0, "Ort einer Handlung → で."),
            MC("こうえん＿犬がいます。", ["に", "で", "を", "と"], 0, "Ort des Vorhandenseins → に.")])

g(0, "[Person] と V", "mit jemandem (と)",
  "[Person] + と + Verb.",
  "と bedeutet „(zusammen) mit“ einer Person.",
  [B("ともだちとえいがを見ます。", "Tomodachi to eiga o mimasu.", "Ich sehe mit Freunden einen Film."),
   B("イースターに、おばあさんとあいました。", "Īsutā ni, obāsan to aimashita.", "Zu Ostern habe ich meine Oma getroffen.")],
  lang="と kann auch zwei Nomen vollständig verbinden („A und B“): パンとコーヒー. Mit einer Person vor einem Verb heißt es „mit“. Allein: ひとりで.",
  uebungen=[MC("かぞく＿りょこうします。", ["と", "を", "が", "は"], 0, "mit jemandem → と.")])

g(0, "[Mittel] で V", "Mittel / Werkzeug (で)",
  "[Verkehrsmittel／Sprache／Werkzeug] + で + Verb.",
  "で nennt das Mittel: でんしゃで (mit dem Zug), 日本語で (auf Japanisch).",
  [B("まい日でんしゃでかいしゃへ行きます。", "Mainichi densha de kaisha e ikimasu.", "Ich fahre jeden Tag mit dem Zug zur Firma."),
   B("日本語ではなしてください。", "Nihongo de hanashite kudasai.", "Bitte sprechen Sie auf Japanisch.")],
  lang="Wer zu Fuß geht, sagt あるいて (ohne で). Die Frage nach dem Mittel lautet なんで (womit?).",
  fehler=["„Zu Fuß“ ist あるいて, nicht あるいてで."],
  uebungen=[MC("じてん車＿がっこうへいきます。", ["で", "を", "に", "が"], 0, "Verkehrsmittel → で.")])

g(0, "V ます／ました", "Verbformen: Verneinung & Vergangenheit",
  "V-ます → V-ません (nicht) · V-ました (Vergangenheit) · V-ませんでした (verneinte Vergangenheit).",
  "Die höfliche ます-Form wird nur am Ende verändert.",
  [B("私はコーヒーをのみません。", "Watashi wa kōhī o nomimasen.", "Ich trinke keinen Kaffee."),
   B("きのう、ハンバーガーをたべました。", "Kinō, hanbāgā o tabemashita.", "Gestern habe ich einen Hamburger gegessen."),
   B("せんしゅうまつ、どこへも行きませんでした。", "Senshūmatsu, doko e mo ikimasen deshita.", "Letztes Wochenende bin ich nirgendwohin gegangen.")],
  lang="Alle Verben folgen demselben Muster: ます → ません → ました → ませんでした. Die Gegenwartsform drückt auch die Zukunft aus (あした行きます = ich gehe morgen).",
  uebungen=[MC("Vergangenheit von たべます:", ["たべました", "たべません", "たべませんでした", "たべましょう"], 0, "ます → ました."),
            CL("きのう、テレビを見＿。（nicht gesehen）", "ませんでした", "verneinte Vergangenheit → ませんでした.")])

g(0, "い-Adj. / な-Adj. + です", "Adjektive (Gegenwart)",
  "い-Adj.: たかいです／たかくないです · な-Adj.: きれいです／きれいじゃありません · vor Nomen: たかい車, きれいな花.",
  "Japanische Adjektive haben zwei Gruppen: い-Adjektive und な-Adjektive.",
  [B("この車はたかいです。", "Kono kuruma wa takai desu.", "Dieses Auto ist teuer."),
   B("あの人はゆうめいな先生です。", "Ano hito wa yūmei na sensei desu.", "Diese Person ist ein(e) berühmte(r) Lehrer(in).")],
  lang="い-Adjektive enden auf い und werden selbst konjugiert (たかい → たかくない). な-Adjektive brauchen vor einem Nomen な (きれいな花) und werden über です verneint (きれいじゃありません). Achtung: きれい und ゆうめい sind な-Adjektive, obwohl sie auf い enden. いい wird zu よくない.",
  fehler=["きれい ist ein な-Adjektiv: きれいな花, nicht きれい花.", "いい → よくないです (nicht いくないです)."],
  uebungen=[MC("Verneinung von たかいです:", ["たかくないです", "たかいじゃありません", "たかくありませんでした", "たかいません"], 0, "い-Adj.: い → くない."),
            MC("きれい＿花", ["な", "の", "い", "—"], 0, "な-Adjektiv vor Nomen → な.")])

g(0, "N が すき です", "mögen (すき)",
  "[Person] は N が すきです／すきじゃありません。 だいすき = sehr mögen.",
  "Das, was man mag, wird mit が markiert.",
  [B("私はねこがすきです。", "Watashi wa neko ga suki desu.", "Ich mag Katzen."),
   B("先生は日本のうたがすきです。", "Sensei wa Nihon no uta ga suki desu.", "Der Lehrer mag japanische Lieder.")],
  lang="すき ist ein な-Adjektiv („beliebt“). Deshalb: すきな人 (Person, die man mag), すきじゃありません (mag nicht). Das Gemochte steht mit が, nicht mit を.",
  fehler=["Nicht を: ねこがすきです (nicht ねこをすきです)."],
  uebungen=[MC("私はすし＿すきです。", ["が", "を", "に", "で"], 0, "Gemochtes → が.")])

g(0, "N1 のほうが N2 より ～", "Vergleich (どちら / ～のほうが～より)",
  "Frage: N1 と N2 と どちらが ～ですか。 Antwort: N1 の ほうが (N2 より) ～です。",
  "より = „als“; のほうが hebt den Gewinner des Vergleichs hervor.",
  [B("日本とかんこくとどちらが大きいですか。", "Nihon to Kankoku to dochira ga ōkii desu ka.", "Was ist größer, Japan oder Korea?"),
   B("日本のほうがかんこくより大きいです。", "Nihon no hō ga Kankoku yori ōkii desu.", "Japan ist größer als Korea."),
   B("車のほうがちかてつよりはやいです。", "Kuruma no hō ga chikatetsu yori hayai desu.", "Das Auto ist schneller als die U-Bahn.")],
  lang="Beim Vergleich von zwei Dingen fragt man mit どちら (welches von beiden). In der Antwort steht der Gewinner mit のほうが, das Verglichene mit より. より allein reicht auch: 日本はかんこくより大きいです.",
  fehler=["より steht nach dem Verglichenen, nicht nach dem Gewinner."],
  uebungen=[MC("日本＿ほうがかんこくより大きいです。", ["の", "は", "が", "を"], 0, "N の ほうが …"),
            CL("ちゅうごくは日本＿大きいです。（größer als Japan）", "より", "より = als.")])

g(0, "N の 中で N が いちばん ～", "Superlativ (いちばん)",
  "[Gruppe] の 中で、N が いちばん ～です。 Frage: [Gruppe] の 中で、なに／だれ／どこ が いちばん ～ですか。",
  "いちばん = „am meisten / Nummer eins“.",
  [B("日本りょうりの中で、なにがいちばんすきですか。", "Nihon ryōri no naka de, nani ga ichiban suki desu ka.", "Was magst du am liebsten von der japanischen Küche?"),
   B("てんぷらがいちばんすきです。", "Tenpura ga ichiban suki desu.", "Tempura mag ich am liebsten."),
   B("ふじ山は日本でいちばん高い山です。", "Fujisan wa Nihon de ichiban takai yama desu.", "Der Fuji ist der höchste Berg Japans.")],
  lang="Der Rahmen steht mit の中で (unter …) oder einfach mit で (in Japan: 日本で). Danach folgt das Gewinner-Nomen mit が und いちばん + Adjektiv.",
  uebungen=[MC("くだものの中で、なに＿いちばんすきですか。", ["が", "を", "は", "に"], 0, "Fragewort + が bei いちばん.")])

g(0, "なにも／どこへも／だれも + Verneinung", "nichts / nirgendwohin / niemand",
  "Fragewort + も + verneintes Verb: なにも～ません, どこへも～ません, だれも～ません.",
  "Mit も und Verneinung wird aus dem Fragewort „nichts / nirgendwo(hin) / niemand“.",
  [B("きのう、なにもたべませんでした。", "Kinō, nani mo tabemasen deshita.", "Gestern habe ich nichts gegessen."),
   B("なつ休みはどこへも行きませんでした。", "Natsuyasumi wa doko e mo ikimasen deshita.", "In den Sommerferien bin ich nirgendwohin gefahren."),
   B("きょうしつにだれもいません。", "Kyōshitsu ni dare mo imasen.", "Im Klassenzimmer ist niemand.")],
  lang="Das Verb muss verneint sein — anders als im Deutschen gibt es eine doppelte Verneinung: なにも + ません. Mit へ／に: どこへも, mit Lebewesen: だれも.",
  fehler=["Das Verb muss verneint sein: なにもたべません (nicht なにもたべます)."],
  uebungen=[MC("デパートへいきました。でも、なにも＿。", ["かいませんでした", "かいました", "かいます", "かいましょう"], 0, "なにも + Verneinung."),
            CL("へやにだれ＿いません。", "も", "だれも + Verneinung = niemand.")])

g(0, "～ませんか／～ましょう", "Vorschlag & Einladung",
  "V-ます → V-ませんか (Wollen wir nicht …?) · V-ましょう (Lass uns …!)",
  "ませんか lädt höflich ein; ましょう schlägt vor oder nimmt die Einladung an.",
  [B("いっしょにおちゃをのみませんか。", "Issho ni ocha o nomimasen ka.", "Wollen wir nicht zusammen Tee trinken?"),
   B("ええ、のみましょう。", "Ē, nomimashō.", "Ja, lass uns trinken!"),
   B("明日の四時にあいましょう。", "Ashita no yo-ji ni aimashō.", "Treffen wir uns morgen um vier.")],
  lang="Die verneinte Frage ませんか ist eine höfliche Einladung — die andere Person kann leicht absagen (ちょっと…). ましょう ist direkter: „Lass uns …“. Achtung: ましょうか (L4) bietet Hilfe an.",
  kontrast=[{'a': 'のみませんか', 'b': 'のみましょう', 'note': 'ませんか = Einladung (Frage), ましょう = Vorschlag/Zusage.'}],
  uebungen=[MC("いっしょにえいがを見＿。（Einladung）", ["ませんか", "ましょうか", "ません", "ました"], 0, "Einladung → ませんか.")])

g(0, "～から、～", "Begründung (weil … / どうして)",
  "Grund + から、Folge。 Frage: どうして ～か。 Antwort: ～から。",
  "から nach einem Satz bedeutet „weil“; der Grund steht vorn.",
  [B("どうして日本へ行きたいですか。", "Dōshite Nihon e ikitai desu ka.", "Warum möchtest du nach Japan?"),
   B("すしがすきですから。", "Sushi ga suki desu kara.", "Weil ich Sushi mag."),
   B("その車はたかいですから、かいません。", "Sono kuruma wa takai desu kara, kaimasen.", "Weil das Auto teuer ist, kaufe ich es nicht.")],
  lang="Im Japanischen steht der Grund vor der Folge: „teuer, weil — kaufe nicht“. Auf eine Frage mit どうして antwortet man mit ～から。. Das deutsche „deshalb“ entspricht derselben Struktur.",
  fehler=["Reihenfolge: Grund + から + Folge (nicht umgekehrt)."],
  uebungen=[MC("さむいです＿、まどをしめます。", ["から", "まで", "より", "が"], 0, "Grund + から."),
            MC("„Warum?“ heißt …", ["どうして", "どこ", "いつ", "だれ"], 0, "どうして = warum.")])

g(0, "N1 に N2 を あげます／もらいます", "geben & bekommen",
  "[Empfänger] に N を あげます · [Geber] に／から N を もらいます · (mir) くれます.",
  "あげます = (weg)geben, もらいます = bekommen; に markiert die andere Person.",
  [B("私はクリスマスに子どもに本をあげました。", "Watashi wa Kurisumasu ni kodomo ni hon o agemashita.", "Ich habe meinem Kind zu Weihnachten ein Buch geschenkt."),
   B("子どもはサンタクロースにプレゼントをもらいました。", "Kodomo wa Santakurōsu ni purezento o moraimashita.", "Das Kind hat vom Weihnachtsmann ein Geschenk bekommen.")],
  lang="Bei あげます steht der Empfänger mit に, bei もらいます der Geber mit に oder から. Gibt jemand MIR etwas, sagt man くれます: ともだちが私にプレゼントをくれました.",
  kontrast=[{'a': 'あげます', 'b': 'もらいます', 'note': 'あげます: ich → andere; もらいます: ich bekomme von anderen.'}],
  uebungen=[MC("ともだち＿プレゼントをあげました。", ["に", "を", "で", "が"], 0, "Empfänger → に.")])

g(0, "Fragewörter", "Fragewörter (いつ・どこ・だれ …)",
  "いつ (wann) · どこ (wo) · だれ (wer) · だれと (mit wem) · なに／なん (was) · なんで (womit) · どうして (warum) · いくら (wie viel) · なんさい (wie alt) · なんようび (welcher Wochentag) · どんな (was für ein)",
  "Das Fragewort steht dort, wo in der Antwort die Information steht; か am Ende.",
  [B("いつ日本へ行きますか。", "Itsu Nihon e ikimasu ka.", "Wann fährst du nach Japan?"),
   B("だれとえいがを見ましたか。", "Dare to eiga o mimashita ka.", "Mit wem hast du den Film gesehen?"),
   B("このかばんはいくらですか。", "Kono kaban wa ikura desu ka.", "Wie viel kostet diese Tasche?")],
  lang="Fragewörter verbinden sich mit Partikeln: だれと (mit wem), どこで (wo — Handlung), どこへ (wohin), なんで (womit). Vor einem Fragewort als Subjekt steht が, nie は: だれがきましたか.",
  fehler=["Nach Fragewort als Subjekt が, nicht は: だれがいますか."],
  uebungen=[MC("＿日本へ行きますか。…らいねん行きます。", ["いつ", "どこ", "だれ", "いくら"], 0, "Zeit → いつ."),
            MC("＿とえいがを見ましたか。…ともだちと。", ["だれ", "なに", "どこ", "いつ"], 0, "mit wem → だれと.")])

# ======================= Lektion 1 =======================
g(1, "V たいです", "etwas tun möchten (～たい)",
  "V-ます → ます streichen + たいです (たべます → たべたいです). Verneinung: たくないです · Vergangenheit: たかったです · verneinte Vergangenheit: たくなかったです.",
  "～たい drückt den eigenen Wunsch aus, etwas zu tun.",
  [B("私はにほんへ行きたいです。", "Watashi wa Nihon e ikitai desu.", "Ich möchte nach Japan fahren."),
   B("きょうはべんきょうしたくないです。", "Kyō wa benkyō shitakunai desu.", "Heute möchte ich nicht lernen."),
   B("子どもの時、ピアノをならいたかったです。", "Kodomo no toki, piano o naraitakatta desu.", "Als Kind wollte ich Klavier lernen.")],
  extra=[B("なつ休みに、どこへ行きたいですか。", "Natsuyasumi ni, doko e ikitai desu ka.", "Wohin möchtest du in den Sommerferien fahren?"),
         B("きょうはラーメンがたべたいです。", "Kyō wa rāmen ga tabetai desu.", "Heute möchte ich Ramen essen.")],
  lang="～たい verhält sich wie ein い-Adjektiv: たい → たくない → たかった → たくなかった. Es beschreibt nur den eigenen Wunsch (oder den des Gesprächspartners in einer Frage). Das Objekt kann mit を oder が stehen: すしを／がたべたいです.",
  fehler=["Nicht für Dritte benutzen: „Er möchte …“ wird anders ausgedrückt.", "Verneinung: たくないです, nicht たいじゃありません."],
  kontrast=[{'a': 'V-たいです', 'b': 'N が ほしいです', 'note': 'たい = etwas TUN wollen, ほしい = etwas HABEN wollen.'}],
  uebungen=[MC("すしを＿たいです。", ["たべ", "たべます", "たべて", "たべる"], 0, "ます-Stamm + たい."),
            MC("Verneinung von 行きたいです:", ["行きたくないです", "行きたいじゃありません", "行きませんたい", "行きたかったです"], 0, "たい → たくない."),
            CL("子どもの時、ピアノをならい＿。（wollte）", "たかったです", "Vergangenheit: たかったです.")])

g(1, "N が ほしいです", "etwas haben möchten (ほしい)",
  "N が ほしいです · Verneinung: ほしくないです · Vergangenheit: ほしかったです · verneinte Vergangenheit: ほしくなかったです.",
  "ほしい ist ein い-Adjektiv: „haben wollen“. Das Gewünschte steht mit が.",
  [B("私は新しいけいたいでんわがほしいです。", "Watashi wa atarashii keitai denwa ga hoshii desu.", "Ich möchte ein neues Handy."),
   B("今、なにがいちばんほしいですか。", "Ima, nani ga ichiban hoshii desu ka.", "Was möchtest du jetzt am liebsten haben?"),
   B("子どもの時、赤いじてん車がほしかったです。", "Kodomo no toki, akai jitensha ga hoshikatta desu.", "Als Kind wollte ich ein rotes Fahrrad.")],
  extra=[B("お金はほしくないです。じかんがほしいです。", "Okane wa hoshikunai desu. Jikan ga hoshii desu.", "Ich will kein Geld. Ich will Zeit.")],
  lang="ほしい wird wie jedes い-Adjektiv konjugiert: ほしい → ほしくない → ほしかった → ほしくなかった. Wie bei すき steht das Gewünschte mit が. Für Handlungen nimmt man ～たい.",
  fehler=["Gewünschtes mit が, nicht を.", "Für Handlungen nicht ほしい, sondern ～たい."],
  uebungen=[MC("新しいかばん＿ほしいです。", ["が", "を", "に", "で"], 0, "Gewünschtes → が."),
            MC("„Ich wollte keinen Hund.“", ["犬はほしくなかったです", "犬がほしかったです", "犬がほしくないです", "犬をほしいです"], 0, "verneinte Vergangenheit → ほしくなかったです.")])

g(1, "子どもの 時、～", "als ich Kind war (～の時)",
  "N の 時、～ (子どもの時 = als ich Kind war; 学生の時 = als ich Student war).",
  "時 (とき) bedeutet „Zeit, als“; mit の hängt es an ein Nomen.",
  [B("子どもの時、レゴであそびました。", "Kodomo no toki, Rego de asobimashita.", "Als Kind habe ich mit Lego gespielt."),
   B("学生の時、まい日、本をよみました。", "Gakusei no toki, mainichi, hon o yomimashita.", "Als Student(in) habe ich jeden Tag Bücher gelesen.")],
  lang="Die Zeit des Hauptsatzes richtet sich nach dem Satzende: 子どもの時、～ました. Weitere Beispiele: 休みの時 (in den Ferien), びょうきの時 (wenn man krank ist).",
  uebungen=[MC("子ども＿時、ピアノをならいました。", ["の", "は", "が", "に"], 0, "N の 時.")])

# ======================= Lektion 3 =======================
g(3, "Verbgruppen I / II / III", "Verbgruppen bestimmen",
  "Gruppe I: -i-ます (いきます, のみます, かきます, まちます …) · Gruppe II: -e-ます (たべます, あけます) + einige -i-ます (みます, おきます, ねます, います, あびます, かります) · Gruppe III: します, きます (und N + します).",
  "Die Gruppe entscheidet, wie die て-Form und die ない-Form gebildet werden.",
  [B("のみます → Gruppe I", "nomimasu → Gruppe I", "trinken: Gruppe I"),
   B("たべます → Gruppe II", "tabemasu → Gruppe II", "essen: Gruppe II"),
   B("べんきょうします → Gruppe III", "benkyō shimasu → Gruppe III", "lernen: Gruppe III")],
  lang="Faustregel: Steht vor ます ein Laut auf -e (たべ, あけ, しめ), ist es Gruppe II. Steht dort ein -i-Laut (のみ, かき, まち), ist es meistens Gruppe I — aber einige häufige Verben sind Ausnahmen und gehören zu Gruppe II: みます, ねます, おきます (aufstehen), います, あびます, かります, きます (anziehen). Gruppe III sind nur します (auch べんきょうします usw.) und きます (kommen).",
  fehler=["おきます (aufstehen) ist Gruppe II, おきます (hinlegen) ist Gruppe I — gleiche Kana, verschiedene Verben.", "みます und ねます sind Gruppe II, obwohl vor ます ein i-Laut steht."],
  uebungen=[MC("Zu welcher Gruppe gehört まちます?", ["I", "II", "III"], 0, "-i-ます, keine Ausnahme → Gruppe I."),
            MC("Zu welcher Gruppe gehört みます?", ["II", "I", "III"], 0, "みます ist eine Ausnahme → Gruppe II."),
            MC("Zu welcher Gruppe gehört そうじします?", ["III", "I", "II"], 0, "N + します → Gruppe III.")])

g(3, "V て-Form", "て-Form bilden",
  "Gruppe I: い/ち/り-ます → って · み/び/に-ます → んで · き-ます → いて · ぎ-ます → いで · し-ます → して · Ausnahme: いきます → いって. Gruppe II: ます → て. Gruppe III: します → して, きます → きて.",
  "Die て-Form ist die Grundlage für ～てください, ～ています, ～てもいいです und für Satzverbindungen.",
  [B("かいます → かって · まちます → まって · とります → とって", "kaimasu → katte · machimasu → matte · torimasu → totte", "って-Gruppe"),
   B("のみます → のんで · よびます → よんで · しにます → しんで", "nomimasu → nonde · yobimasu → yonde · shinimasu → shinde", "んで-Gruppe"),
   B("かきます → かいて · いそぎます → いそいで · はなします → はなして", "kakimasu → kaite · isogimasu → isoide · hanashimasu → hanashite", "いて／いで／して"),
   B("たべます → たべて · します → して · きます → きて", "tabemasu → tabete · shimasu → shite · kimasu → kite", "Gruppe II und III")],
  lang="Merksatz für Gruppe I nach dem Laut vor ます: い・ち・り → って, み・び・に → んで, き → いて, ぎ → いで, し → して. Einzige Ausnahme: いきます → いって. Gruppe II ist einfach: ます durch て ersetzen. Gruppe III: して / きて.",
  fehler=["いきます → いって (nicht いいて).", "Gruppe-II-Verben nicht wie Gruppe I behandeln: みます → みて (nicht みって)."],
  uebungen=[MC("て-Form von まちます:", ["まって", "まちて", "まんで", "まいて"], 0, "ち-ます → って."),
            MC("て-Form von よみます:", ["よんで", "よって", "よみて", "よいて"], 0, "み-ます → んで."),
            MC("て-Form von いきます:", ["いって", "いいて", "いきて", "いんで"], 0, "Ausnahme: いって."),
            CL("いそぎます → いそ＿", "いで", "ぎ-ます → いで.")])

g(3, "N を ください", "Etwas, bitte (beim Bestellen)",
  "N を ください。 (mit Menge: N を 二つ ください)",
  "～をください bittet darum, etwas zu bekommen — z. B. im Restaurant oder Laden.",
  [B("ピザとコーラをください。", "Piza to kōra o kudasai.", "Eine Pizza und eine Cola, bitte."),
   B("すみません、水をください。", "Sumimasen, mizu o kudasai.", "Entschuldigung, Wasser bitte."),
   B("あのかばんをください。", "Ano kaban o kudasai.", "Diese Tasche dort, bitte.")],
  lang="ください steht nach dem Objekt mit を. Mit すみません davor klingt es höflicher. Für Handlungen benutzt man die て-Form: ～てください.",
  kontrast=[{'a': 'N を ください', 'b': 'V-て ください', 'note': 'N を ください = etwas geben lassen; V-て ください = jemanden bitten, etwas zu tun.'}],
  uebungen=[MC("ビール＿ください。", ["を", "が", "に", "で"], 0, "N を ください.")])

g(3, "V-て ください", "Bitte (tun Sie …)",
  "V-て + ください。",
  "Mit der て-Form + ください bittet man jemanden höflich, etwas zu tun.",
  [B("まどをあけてください。", "Mado o akete kudasai.", "Bitte öffnen Sie das Fenster."),
   B("ここでまってください。", "Koko de matte kudasai.", "Bitte warten Sie hier."),
   B("しゃしんをとってください。", "Shashin o totte kudasai.", "Bitte machen Sie ein Foto.")],
  extra=[B("すみません、もういちど言ってください。", "Sumimasen, mō ichido itte kudasai.", "Entschuldigung, bitte sagen Sie es noch einmal."),
         B("でんわばんごうをおしえてください。", "Denwa bangō o oshiete kudasai.", "Bitte sagen Sie mir Ihre Telefonnummer.")],
  lang="～てください ist eine höfliche Bitte oder Anweisung. Mit すみません davor klingt es weicher. Die Verneinung („bitte nicht“) kommt in Lektion 13: ～ないでください.",
  fehler=["て-Form richtig bilden: まちます → まって (nicht まちて)."],
  uebungen=[MC("でんきを＿ください。", ["つけて", "つけます", "つける", "つけ"], 0, "て-Form + ください."),
            CL("ちょっとまっ＿ください。", "て", "まちます → まって."),
            MC("„Bitte helfen Sie mir!“", ["てつだってください", "てつだいてください", "てつだってくださいか", "てつだいます"], 0, "てつだいます → てつだって.")])

g(3, "～から、V-て ください", "Bitte mit Begründung",
  "Grund + から、V-て ください。",
  "Man nennt zuerst den Grund mit から und dann die Bitte.",
  [B("さむいですから、まどをしめてください。", "Samui desu kara, mado o shimete kudasai.", "Weil es kalt ist, schließen Sie bitte das Fenster."),
   B("じかんがありませんから、いそいでください。", "Jikan ga arimasen kara, isoide kudasai.", "Weil wir keine Zeit haben, beeilen Sie sich bitte."),
   B("くらいですから、でんきをつけてください。", "Kurai desu kara, denki o tsukete kudasai.", "Weil es dunkel ist, machen Sie bitte das Licht an.")],
  lang="Wie bei allen から-Sätzen steht der Grund vorn. Das Satzende (～てください) bestimmt, dass es eine Bitte ist.",
  uebungen=[MC("あついです＿、エアコンをつけてください。", ["から", "まで", "より", "や"], 0, "Grund + から.")])

# ======================= Lektion 4 =======================
g(4, "V-ましょうか", "Soll ich …? (Hilfe anbieten)",
  "V-ます → ます streichen + ましょうか。 Antwort: はい、お願いします／～てください。 · いいえ、だいじょうぶです。",
  "～ましょうか bietet an, etwas für jemanden zu tun.",
  [B("でんきをつけましょうか。…はい、つけてください。", "Denki o tsukemashō ka. … Hai, tsukete kudasai.", "Soll ich das Licht anmachen? … Ja, bitte."),
   B("かばんをもちましょうか。…はい、お願いします。", "Kaban o mochimashō ka. … Hai, onegai shimasu.", "Soll ich die Tasche tragen? … Ja, bitte."),
   B("タクシーをよびましょうか。", "Takushī o yobimashō ka.", "Soll ich ein Taxi rufen?")],
  extra=[B("まどをあけましょうか。…はい、あけてください。", "Mado o akemashō ka. … Hai, akete kudasai.", "Soll ich das Fenster öffnen? … Ja, bitte öffnen.")],
  lang="ましょうか ist ein Angebot (Soll ich …?). ましょう (ohne か) ist ein gemeinsamer Vorschlag (Lass uns …). Die Antwort auf ein Angebot ist oft ～てください oder お願いします.",
  kontrast=[{'a': 'もちましょうか', 'b': 'もってください', 'note': 'ましょうか = ich biete an; てください = ich bitte dich.'},
            {'a': 'いきましょう', 'b': 'いきましょうか', 'note': 'ましょう = Lass uns gehen; ましょうか = Sollen wir / soll ich gehen?'}],
  uebungen=[MC("„Soll ich das Fenster öffnen?“", ["まどをあけましょうか", "まどをあけてください", "まどをあけたいです", "まどをあけませんか"], 0, "Angebot → ましょうか."),
            CL("にもつをもち＿。…はい、お願いします。", "ましょうか", "Hilfe anbieten → ましょうか.")])

# ======================= Lektion 5 =======================
g(5, "V-て います (Verlauf)", "gerade etwas tun",
  "V-て + います。 Frage: 今、なにをしていますか。",
  "～ています beschreibt eine Handlung, die gerade abläuft (wie „gerade dabei sein“).",
  [B("やまださんは今、りょうりをしています。", "Yamada-san wa ima, ryōri o shite imasu.", "Herr/Frau Yamada kocht gerade."),
   B("私は今、日本語をべんきょうしています。", "Watashi wa ima, nihongo o benkyō shite imasu.", "Ich lerne gerade Japanisch."),
   B("子どもたちはこうえんであそんでいます。", "Kodomotachi wa kōen de asonde imasu.", "Die Kinder spielen gerade im Park.")],
  extra=[B("今、なにをしていますか。…テレビを見ています。", "Ima, nani o shite imasu ka. … Terebi o mite imasu.", "Was machst du gerade? … Ich sehe fern.")],
  lang="Die て-Form + います entspricht dem englischen -ing: Die Handlung ist im Gange. Verneinung: ～ていません, Vergangenheit: ～ていました (war gerade dabei).",
  fehler=["て-Form richtig bilden: よみます → よんでいます."],
  uebungen=[MC("今、テレビを＿います。", ["見て", "見ます", "見", "見る"], 0, "て-Form + います."),
            CL("やまださんは今、本をよん＿います。", "で", "よみます → よんで.")])

g(5, "V-て います (Gewohnheit)", "etwas regelmäßig / beruflich tun",
  "まいにち／まいしゅう／まいつき／まいとし + V-て います。 Beruf: [Firma] で はたらいています。",
  "～ています drückt auch Gewohnheiten und dauerhafte Tätigkeiten aus.",
  [B("私はまい日しんぶんをよんでいます。", "Watashi wa mainichi shinbun o yonde imasu.", "Ich lese jeden Tag Zeitung."),
   B("シュミットさんはソニーではたらいています。", "Shumitto-san wa Sonī de hataraite imasu.", "Herr/Frau Schmidt arbeitet bei Sony."),
   B("まいしゅう、ジムでヨガをしています。", "Maishū, jimu de yoga o shite imasu.", "Jede Woche mache ich im Fitnessstudio Yoga.")],
  lang="Mit Häufigkeitswörtern (まいにち, まいしゅう …) oder bei Berufen beschreibt ～ています einen andauernden Zustand des Lebens: „ich arbeite (zurzeit) bei …“. Frage nach dem Beruf: どこではたらいていますか。",
  kontrast=[{'a': '今、はたらいています', 'b': 'ソニーではたらいています', 'note': 'Mit 今 = gerade jetzt; mit Firma/Häufigkeit = regelmäßig/beruflich.'}],
  uebungen=[MC("どこで＿いますか。…ソニーで。", ["はたらいて", "はたらきて", "はたらいで", "はたらって"], 0, "はたらきます → はたらいて."),
            MC("„jeden Monat“ heißt …", ["まいつき", "まいとし", "まいしゅう", "まいあさ"], 0, "まいつき = jeden Monat.")])

# ======================= Lektion 6 =======================
g(6, "V-て います (Zustand)", "Zustand / Ergebnis",
  "けっこんしています · すんでいます · もっています · かぜをひいています · しっています",
  "Bei manchen Verben beschreibt ～ています einen Zustand, der nach einer Handlung andauert.",
  [B("私はけっこんしています。", "Watashi wa kekkon shite imasu.", "Ich bin verheiratet."),
   B("ミラーさんは大阪にすんでいます。", "Mirā-san wa Ōsaka ni sunde imasu.", "Herr/Frau Miller wohnt in Osaka."),
   B("かぜをひいていますから、うちで休みます。", "Kaze o hiite imasu kara, uchi de yasumimasu.", "Weil ich erkältet bin, ruhe ich mich zu Hause aus."),
   B("車をもっていますか。…いいえ、もっていません。", "Kuruma o motte imasu ka. … Iie, motte imasen.", "Hast du ein Auto? … Nein, habe ich nicht.")],
  lang="けっこんします heißt „heiraten“ (ein Moment), けっこんしています „verheiratet sein“ (Zustand). Genauso: すみます (sich niederlassen) → すんでいます (wohnen), もちます (in die Hand nehmen) → もっています (besitzen), かぜをひきます (sich erkälten) → ひいています (erkältet sein).",
  fehler=["„Ich bin verheiratet“ ist けっこんしています, nicht けっこんします."],
  uebungen=[MC("„Ich bin verheiratet.“", ["けっこんしています", "けっこんします", "けっこんしました", "けっこんしたいです"], 0, "Zustand → ～ています."),
            CL("私はベルリンにすん＿います。", "で", "すみます → すんで.")])

g(6, "しって います／しりません", "kennen, wissen",
  "Bejahung: しっています · Verneinung: しりません (nicht しっていません).",
  "しります = kennenlernen; den Zustand „kennen/wissen“ drückt しっています aus.",
  [B("ミラーさんをしっていますか。…はい、しっています。", "Mirā-san o shitte imasu ka. … Hai, shitte imasu.", "Kennst du Herrn/Frau Miller? … Ja, kenne ich."),
   B("いいえ、しりません。", "Iie, shirimasen.", "Nein, kenne ich nicht."),
   B("やすこさんのじゅうしょをしっていますか。", "Yasuko-san no jūsho o shitte imasu ka.", "Kennst du Yasukos Adresse?")],
  lang="Eine Besonderheit: Die Bejahung lautet しっています, die Verneinung aber しりません. しっていません klingt falsch.",
  fehler=["Verneinung: しりません, nicht しっていません."],
  uebungen=[MC("あの人をしっていますか。…いいえ、＿。", ["しりません", "しっていません", "しりませんでした", "しっています"], 0, "Verneinung → しりません.")])

g(6, "N を むかえに いきます／きます", "jemanden abholen",
  "[Person] を (Ort へ) むかえに いきます (abholen gehen) ／ きます (abholen kommen).",
  "むかえに いきます = losgehen, um jemanden abzuholen.",
  [B("子どもをむかえにいきます。", "Kodomo o mukae ni ikimasu.", "Ich hole das Kind ab."),
   B("あなたたちを車でえきへむかえにいきますよ。", "Anatatachi o kuruma de eki e mukae ni ikimasu yo.", "Ich hole euch mit dem Auto vom Bahnhof ab."),
   B("父が私をむかえにきました。", "Chichi ga watashi o mukae ni kimashita.", "Mein Vater hat mich abgeholt.")],
  lang="Die abgeholte Person steht mit を, der Ort mit へ oder に. いきます = man geht hin, きます = jemand kommt zu mir.",
  uebungen=[MC("えきへともだちを＿いきます。", ["むかえに", "むかえて", "むかえ", "むかえを"], 0, "むかえに いきます.")])

g(6, "N を もって いきます／きます", "mitnehmen / mitbringen",
  "N を もっていきます (mitnehmen, hin) ／ もってきます (mitbringen, her).",
  "もって (die て-Form von もちます) + いきます／きます.",
  [B("ピクニックに水をもっていきます。", "Pikunikku ni mizu o motte ikimasu.", "Ich nehme Wasser zum Picknick mit."),
   B("あした、ビールをもってきてください。", "Ashita, bīru o motte kite kudasai.", "Bring morgen bitte Bier mit."),
   B("かさをもっていきましょうか。", "Kasa o motte ikimashō ka.", "Soll ich einen Schirm mitnehmen?")],
  lang="Die Richtung entscheidet: von hier weg → もっていきます, zu mir her → もってきます. Beide werden wie いきます bzw. きます konjugiert.",
  kontrast=[{'a': 'もっていきます', 'b': 'もってきます', 'note': 'いきます = von mir weg (mitnehmen), きます = zu mir her (mitbringen).'}],
  uebungen=[MC("„Bitte bring Wasser mit!“", ["水をもってきてください", "水をもっていってください", "水をもちてください", "水をもってください"], 0, "zu mir her → もってきます.")])

# ======================= Lektion 8 =======================
g(8, "V1-て、V2-て、V3-ます", "Handlungsfolge (und dann …)",
  "Alle Verben außer dem letzten in der て-Form; das letzte Verb bestimmt Zeit, Verneinung, Bitte oder Wunsch.",
  "Mit der て-Form reiht man Handlungen in ihrer zeitlichen Reihenfolge aneinander.",
  [B("朝おきて、コーヒーをのみます。", "Asa okite, kōhī o nomimasu.", "Morgens stehe ich auf und trinke Kaffee."),
   B("わたしはおきて、かいしゃへ行って、コーヒーをのみました。", "Watashi wa okite, kaisha e itte, kōhī o nomimashita.", "Ich bin aufgestanden, zur Firma gegangen und habe Kaffee getrunken."),
   B("私はテレビを見て、ピザをたべたいです。", "Watashi wa terebi o mite, piza o tabetai desu.", "Ich möchte fernsehen und Pizza essen.")],
  extra=[B("土よう日にとしょかんへ行って、本をよんで、スーパーでかいものをして、かえります。", "Doyōbi ni toshokan e itte, hon o yonde, sūpā de kaimono o shite, kaerimasu.", "Am Samstag gehe ich in die Bibliothek, lese ein Buch, kaufe im Supermarkt ein und gehe nach Hause."),
         B("きょうとでおてらを見て、おんせんにはいりました。", "Kyōto de otera o mite, onsen ni hairimashita.", "In Kyoto habe ich Tempel angesehen und im Onsen gebadet.")],
  lang="Die て-Form selbst hat keine Zeit. Erst das Verb am Ende sagt, ob es Gegenwart (ます), Vergangenheit (ました), Verneinung (ません), Bitte (てください) oder Wunsch (たいです) ist. Die Reihenfolge der Verben ist die Reihenfolge der Handlungen.",
  fehler=["Nicht jedes Verb in der Vergangenheit: おきて、行って、のみました (nur das letzte!)."],
  uebungen=[MC("朝ごはんを＿、がっこうへ行きます。", ["たべて", "たべます", "たべました", "たべたい"], 0, "Verben in der Kette → て-Form."),
            MC("„Ich bin aufgestanden und habe geduscht.“", ["おきて、シャワーをあびました", "おきました、シャワーをあびて", "おきて、シャワーをあびて", "おきます、シャワーをあびました"], 0, "Nur das letzte Verb trägt die Zeit."),
            CL("ローマへ行っ＿、ピザをたべたいです。", "て", "いきます → いって.")])

# ======================= Lektion 9 =======================
g(9, "い-Adj. Vergangenheit", "い-Adjektive in der Vergangenheit",
  "～い → ～かったです (たかかったです) · Verneinung: ～くなかったです · いい → よかったです／よくなかったです.",
  "い-Adjektive bilden ihre Vergangenheit selbst; です bleibt unverändert.",
  [B("きのうはすずしかったです。", "Kinō wa suzushikatta desu.", "Gestern war es kühl."),
   B("パーティーはおもしろかったですか。…いいえ、おもしろくなかったです。", "Pātī wa omoshirokatta desu ka. … Iie, omoshirokunakatta desu.", "War die Party lustig? … Nein, war sie nicht."),
   B("きのう、てんきはわるかったです。", "Kinō, tenki wa warukatta desu.", "Gestern war das Wetter schlecht.")],
  extra=[B("せんしゅうのテストはむずかしかったです。", "Senshū no tesuto wa muzukashikatta desu.", "Der Test letzte Woche war schwer."),
         B("ホテルはよかったです。", "Hoteru wa yokatta desu.", "Das Hotel war gut.")],
  lang="Die vier Formen: たかいです (ist teuer) · たかくないです (ist nicht teuer) · たかかったです (war teuer) · たかくなかったです (war nicht teuer). Ausnahme いい: よくないです, よかったです, よくなかったです.",
  fehler=["Nicht たかいでした — die Vergangenheit steckt im Adjektiv: たかかったです.", "いい → よかった (nicht いかった)."],
  kontrast=[{'a': 'たかかったです', 'b': 'しずかでした', 'note': 'い-Adj.: Vergangenheit im Adjektiv; な-Adj.: Vergangenheit über でした.'}],
  uebungen=[MC("Vergangenheit von さむいです:", ["さむかったです", "さむいでした", "さむくなかったです", "さむでした"], 0, "い → かったです."),
            MC("Vergangenheit von いいです:", ["よかったです", "いかったです", "いいでした", "よくないです"], 0, "Ausnahme: いい → よかった."),
            CL("ケーキはあま＿。（war nicht süß）", "くなかったです", "verneinte Vergangenheit: くなかったです.")])

g(9, "な-Adj. Vergangenheit", "な-Adjektive in der Vergangenheit",
  "～です → ～でした · Verneinung: ～じゃ／ではありませんでした.",
  "な-Adjektive (und Nomen) bilden die Vergangenheit über です.",
  [B("きょうとはきれいでした。", "Kyōto wa kirei deshita.", "Kyoto war schön."),
   B("先生はしんせつじゃありませんでした。", "Sensei wa shinsetsu ja arimasen deshita.", "Der Lehrer war nicht freundlich."),
   B("ホテルはしずかでした。", "Hoteru wa shizuka deshita.", "Das Hotel war ruhig.")],
  lang="Die vier Formen: しずかです · しずかじゃありません · しずかでした · しずかじゃありませんでした. Genauso bei Nomen: 学生でした (war Student). Achtung bei きれい, ゆうめい, しんせつ — sie sind な-Adjektive.",
  fehler=["きれい ist ein な-Adjektiv: きれいでした (nicht きれかったです)."],
  uebungen=[MC("Vergangenheit von べんりです:", ["べんりでした", "べんりかったです", "べんりくなかったです", "べんりいでした"], 0, "な-Adj. → でした."),
            MC("„Die Stadt war nicht belebt.“", ["まちはにぎやかじゃありませんでした", "まちはにぎやかくなかったです", "まちはにぎやかでした", "まちはにぎやかじゃありません"], 0, "な-Adj. verneinte Vergangenheit.")])

g(9, "N1 か N2", "oder (A oder B)",
  "N1 か N2 (を) ～",
  "か zwischen zwei Nomen bedeutet „oder“.",
  [B("すしかラーメンをたべたいです。", "Sushi ka rāmen o tabetai desu.", "Ich möchte Sushi oder Ramen essen."),
   B("あるいてかじてん車でかいしゃへ行きたいです。", "Aruite ka jitensha de kaisha e ikitai desu.", "Ich möchte zu Fuß oder mit dem Fahrrad zur Firma."),
   B("赤いじてん車か青いじてん車をかいます。", "Akai jitensha ka aoi jitensha o kaimasu.", "Ich kaufe ein rotes oder ein blaues Fahrrad.")],
  lang="Am Satzende macht か eine Frage, zwischen zwei Nomen bedeutet es „oder“.",
  uebungen=[MC("コーヒー＿おちゃをのみます。（oder）", ["か", "と", "や", "も"], 0, "か = oder.")])

# ======================= Lektion 10 =======================
g(10, "い-Adj.-くて、～", "い-Adjektive verbinden (und)",
  "～い → ～くて (たかい → たかくて) · いい → よくて.",
  "Mit der くて-Form verbindet man ein い-Adjektiv mit weiteren Adjektiven oder Sätzen.",
  [B("このくるまはたかくて、はやくて、きれいです。", "Kono kuruma wa takakute, hayakute, kirei desu.", "Dieses Auto ist teuer, schnell und schön."),
   B("おくさんのケーキはあまくて、おいしかったです。", "Okusan no kēki wa amakute, oishikatta desu.", "Der Kuchen Ihrer Frau war süß und lecker."),
   B("私のねこはまるくて、かわいいです。", "Watashi no neko wa marukute, kawaii desu.", "Meine Katze ist rund und süß.")],
  extra=[B("ラーメンはやすくて、おいしいです。", "Rāmen wa yasukute, oishii desu.", "Ramen ist billig und lecker."),
         B("きょうしつはせまくて、くらいです。", "Kyōshitsu wa semakute, kurai desu.", "Das Klassenzimmer ist eng und dunkel.")],
  lang="Wie bei Verben trägt nur das letzte Glied die Zeit: あまくて、おいしかったです (war süß und lecker). Statt そして kann man so mehrere Eigenschaften in einem Satz nennen.",
  fehler=["いい → よくて (nicht いくて).", "Nur das letzte Adjektiv trägt die Vergangenheit."],
  kontrast=[{'a': 'やすくて', 'b': 'しずかで', 'note': 'い-Adj. → くて, な-Adj./Nomen → で.'}],
  uebungen=[MC("このへやはひろ＿、あかるいです。", ["くて", "で", "いで", "いくて"], 0, "い-Adj. → くて."),
            MC("„gut und billig“", ["よくて、やすい", "いくて、やすい", "いいで、やすい", "よいで、やすい"], 0, "いい → よくて.")])

g(10, "な-Adj./N で、～", "な-Adjektive und Nomen verbinden",
  "な-Adj. + で (しずかで) · Nomen + で (学生で).",
  "な-Adjektive und Nomen werden mit で verbunden.",
  [B("トムさんはハンサムで、しんせつです。", "Tomu-san wa hansamu de, shinsetsu desu.", "Tom ist gutaussehend und freundlich."),
   B("ホテルはしずかで、きれいでした。", "Hoteru wa shizuka de, kirei deshita.", "Das Hotel war ruhig und sauber."),
   B("とうきょうはにぎやかで、おもしろくて、よかったです。", "Tōkyō wa nigiyaka de, omoshirokute, yokatta desu.", "Tokio war lebhaft, interessant und toll.")],
  lang="Die Formen lassen sich mischen: にぎやかで (な) + おもしろくて (い) + よかったです. Das Satzende bestimmt Zeit und Verneinung.",
  uebungen=[MC("この町はしずか＿、きれいです。", ["で", "くて", "な", "に"], 0, "な-Adj. → で."),
            CL("ふじ山はゆうめい＿、きれいです。", "で", "ゆうめい ist ein な-Adjektiv → で.")])

# ======================= Lektion 11 =======================
g(11, "V-て も いいです", "dürfen (Erlaubnis)",
  "V-て + もいいです。 Frage: V-て もいいですか。 Antwort: はい、いいですよ／どうぞ。",
  "～てもいいです erlaubt etwas; mit か fragt man um Erlaubnis („Darf ich …?“).",
  [B("ここでしゃしんをとってもいいですか。…はい、どうぞ。", "Koko de shashin o totte mo ii desu ka. … Hai, dōzo.", "Darf ich hier fotografieren? … Ja, bitte."),
   B("私はらいしゅう、月よう日に休んでもいいですか。", "Watashi wa raishū, getsuyōbi ni yasunde mo ii desu ka.", "Darf ich nächste Woche am Montag freinehmen?"),
   B("このいすにすわってもいいですよ。", "Kono isu ni suwatte mo ii desu yo.", "Du darfst dich auf diesen Stuhl setzen.")],
  extra=[B("まどをあけてもいいですか。…はい、いいですよ。", "Mado o akete mo ii desu ka. … Hai, ii desu yo.", "Darf ich das Fenster öffnen? … Ja, gern."),
         B("あなたのペンをつかってもいいですか。", "Anata no pen o tsukatte mo ii desu ka.", "Darf ich deinen Stift benutzen?")],
  lang="Wörtlich: „Auch wenn ich … tue, ist es gut.“ Antwort bei Ja: はい、いいですよ／どうぞ. Bei Nein höflich: すみません、ちょっと… oder streng: いいえ、～てはいけません.",
  fehler=["て-Form richtig: すいます → すって, すわります → すわって."],
  kontrast=[{'a': 'V-てもいいです', 'b': 'V-てはいけません', 'note': 'もいいです = dürfen, はいけません = nicht dürfen.'}],
  uebungen=[MC("ここでタバコをすって＿いいですか。", ["も", "は", "を", "が"], 0, "Erlaubnis → ても いいです."),
            MC("„Darf ich hier sitzen?“", ["ここにすわってもいいですか", "ここにすわってはいけません", "ここにすわってください", "ここにすわりましょうか"], 0, "Erlaubnis fragen → てもいいですか."),
            CL("このでんわをつかっ＿もいいですか。", "て", "つかいます → つかって.")])

g(11, "V-て は いけません", "nicht dürfen (Verbot)",
  "V-て + はいけません。",
  "～てはいけません verbietet etwas („Man darf nicht …“).",
  [B("ここでタバコをすってはいけません。", "Koko de tabako o sutte wa ikemasen.", "Hier darf man nicht rauchen."),
   B("としょかんでアイスをたべてはいけません。", "Toshokan de aisu o tabete wa ikemasen.", "In der Bibliothek darf man kein Eis essen."),
   B("このへやにはいってはいけません。", "Kono heya ni haitte wa ikemasen.", "Dieses Zimmer darf man nicht betreten.")],
  extra=[B("子どもは一人で川であそんではいけません。", "Kodomo wa hitori de kawa de asonde wa ikemasen.", "Kinder dürfen nicht allein am Fluss spielen.")],
  lang="は wird hier „wa“ gesprochen. ～てはいけません ist ein klares, eher strenges Verbot (Schilder, Regeln). Höflicher bittet man mit ～ないでください (Lektion 13).",
  fehler=["は wird „wa“ gesprochen.", "Nicht ～てもいけません — Verbot ist ～ては いけません."],
  uebungen=[MC("ここでしゃしんをとって＿いけません。", ["は", "も", "を", "が"], 0, "Verbot → ては いけません."),
            MC("„Du darfst den Hund nicht anfassen.“", ["犬にさわってはいけません", "犬にさわってもいいです", "犬にさわってください", "犬にさわりたいです"], 0, "Verbot → てはいけません.")])

# ======================= Lektion 12 =======================
g(12, "ちょっと…", "höfliche Absage (ちょっと…)",
  "Einladung／Bitte → すみません、[Zeit／Sache] は ちょっと…。",
  "Mit ちょっと… (eigentlich „ein bisschen“) lehnt man höflich ab, ohne nein zu sagen.",
  [B("あした、いっしょにテニスをしませんか。…すみません、あしたはちょっと…。", "Ashita, issho ni tenisu o shimasen ka. … Sumimasen, ashita wa chotto….", "Wollen wir morgen zusammen Tennis spielen? … Tut mir leid, morgen passt es nicht so gut."),
   B("このでんわをつかってもいいですか。…すみません、ちょっと…。", "Kono denwa o tsukatte mo ii desu ka. … Sumimasen, chotto….", "Darf ich dieses Telefon benutzen? … Entschuldigung, das ist schwierig.")],
  lang="Ein direktes いいえ klingt im Japanischen oft unhöflich. Man sagt stattdessen すみません + ちょっと… und lässt den Satz offen; der Gesprächspartner versteht die Absage.",
  uebungen=[MC("Wie sagt man höflich ab?", ["すみません、ちょっと…", "いいえ、いきません", "はい、いきましょう", "いいですよ"], 0, "ちょっと… = höfliche Absage.")])

# ======================= Lektion 13 =======================
g(13, "V ない-Form", "ない-Form bilden",
  "Gruppe I: -i-ます → -a-ない (いきます → いかない; Laut い → わ: かいます → かわない) · Gruppe II: ます → ない (たべます → たべない) · Gruppe III: します → しない, きます → こない.",
  "Die ない-Form ist die einfache Verneinung; sie wird für ～ないでください gebraucht.",
  [B("いきます → いかない · のみます → のまない · まちます → またない", "ikimasu → ikanai · nomimasu → nomanai · machimasu → matanai", "Gruppe I: i → a"),
   B("かいます → かわない · すいます → すわない", "kaimasu → kawanai · suimasu → suwanai", "Gruppe I: い → わ"),
   B("たべます → たべない · ねます → ねない · おきます → おきない", "tabemasu → tabenai · nemasu → nenai · okimasu → okinai", "Gruppe II"),
   B("します → しない · きます → こない", "shimasu → shinai · kimasu → konai", "Gruppe III")],
  lang="Bei Gruppe I wird der i-Laut vor ます zum a-Laut: か(き)→か, の(み)→ま, ま(ち)→た. Endet der Stamm auf い, wird daraus わ (かいます → かわない, あいます → あわない). Gruppe II: einfach ます → ない. Gruppe III unregelmäßig: しない, こない.",
  fehler=["かいます → かわない (nicht かあない).", "きます (kommen) → こない (nicht きない).", "おきます (aufstehen, Gr. II) → おきない."],
  uebungen=[MC("ない-Form von のみます:", ["のまない", "のみない", "のんない", "のまらない"], 0, "Gruppe I: み → ま."),
            MC("ない-Form von かいます:", ["かわない", "かあない", "かいない", "かない"], 0, "い → わ."),
            MC("ない-Form von きます (kommen):", ["こない", "きない", "かない", "くない"], 0, "Gruppe III: こない."),
            CL("たべます → たべ＿", "ない", "Gruppe II: ます → ない.")])

g(13, "V-ないで ください", "Bitte nicht … (negative Bitte)",
  "V-ない + でください。",
  "～ないでください bittet jemanden höflich, etwas nicht zu tun.",
  [B("このいすにすわらないでください。", "Kono isu ni suwaranai de kudasai.", "Bitte setzen Sie sich nicht auf diesen Stuhl."),
   B("きんえんですから、たばこをすわないでください。", "Kin'en desu kara, tabako o suwanai de kudasai.", "Hier ist Rauchverbot, bitte rauchen Sie nicht."),
   B("私をまたないでください。おそくなりますから。", "Watashi o matanai de kudasai. Osoku narimasu kara.", "Bitte warte nicht auf mich. Ich komme später."),
   B("とりにごはんをあげないでください。", "Tori ni gohan o agenai de kudasai.", "Bitte füttern Sie die Vögel nicht.")],
  extra=[B("あぶないですから、おさないでください。", "Abunai desu kara, osanai de kudasai.", "Weil es gefährlich ist, bitte nicht drücken."),
         B("しんぱいしないでください。", "Shinpai shinai de kudasai.", "Bitte mach dir keine Sorgen.")],
  lang="Gegenstück zu ～てください. Höflicher als ～てはいけません, weil es eine Bitte und kein Verbot ist. Mit から davor nennt man den Grund.",
  kontrast=[{'a': 'あけてください', 'b': 'あけないでください', 'note': 'てください = bitte tun, ないでください = bitte nicht tun.'},
            {'a': 'すわないでください', 'b': 'すってはいけません', 'note': 'ないでください = höfliche Bitte, てはいけません = Verbot.'}],
  uebungen=[MC("ここでしゃしんを＿ください。（bitte nicht）", ["とらないで", "とって", "とらなくて", "とりないで"], 0, "ない-Form + でください."),
            MC("„Bitte vergiss deinen Schirm nicht!“", ["かさをわすれないでください", "かさをわすれてください", "かさをわすれてはいけません", "かさをわすれませんか"], 0, "negative Bitte → ないでください."),
            CL("まどをあけ＿ください。さむいですから。", "ないで", "Gr. II: あけない + でください.")])
