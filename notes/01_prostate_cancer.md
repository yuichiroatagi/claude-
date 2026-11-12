# 前立腺癌 治療方針ノート

| 項目 | 内容 |
|---|---|
| 最終確認日 | 2026-11-12 |
| 主な参照ガイドライン | [EAU-EANM-ESTRO-ESUR-ISUP-SIOG 2026 Part I](https://www.urotoday.com/recent-abstracts/urologic-oncology/prostate-cancer/170648-eau-eanm-estro-esur-isup-siog-guidelines-on-prostate-cancer-2026-update-part-i-screening-diagnosis-and-local-treatment-with-curative-intent.html)／[Part II](https://www.urotoday.com/recent-abstracts/urologic-oncology/prostate-cancer/170649-eau-eanm-estro-esur-isup-siog-guidelines-on-prostate-cancer-part-ii-2026-update-treatment-of-relapsing-and-metastatic-prostate-cancer.html)／NCCN Prostate／日本泌尿器科学会 前立腺癌診療ガイドライン |
| ステータス | 初版確定 |

**凡例**
- **方針**（黒字）：自分の現在のコンセンサス
- **参考**：ガイドライン（GL）・根拠・保険適用
- 赤枠の「Claude 提案」：Claude からの提案・注視事項（リンク付き）。採用したものは「方針」に移す

※ リンクのうち PubMed 検索リンクは、試験名で検索した結果ページに飛ぶ。通常は先頭が該当論文。

---

## 1. スクリーニング・生検適応

**方針**
- 生検前 MRI はルーチンで撮影
- PI-RADS 4 以上は必ず生検
- PI-RADS 3 は PSA と PSAD で判断
  - PSAD 0.15〜0.20 ng/mL/cc 以上：生検を考慮
  - PSA 10 以下かつ PSAD 低値：3 か月後に PSA を再検してフォロー。理想は S2,3PSA% を併用

**参考**
- GL：EAU 2026 は、生検前 MRI で不要な生検を減らすことを推奨。生検するなら標的生検と regional 生検を組み合わせる。PI-RADS 3 では PSAD・バイオマーカー・リスクカリキュレーターでリスクを層別化する
- 保険適用：S2,3PSA% は PSA 4.0〜10.0 ng/mL が対象で、原則 1 回まで。PSA F/T 比・phi と同時に測った場合は主なもの 1 つだけ算定（[厚労省資料](https://www.mhlw.go.jp/content/12404000/000843973.pdf)）。phi は 2021 年 11 月から保険適用

## 2. 低リスク・中間リスク（監視療法）

**方針**
- 対象：GG1、および以下をすべて満たす GG2
  - 陽性コア 2 本以下
  - 陽性率 30% 未満
  - pattern 4 が 10% 未満
  - cribriform・IDC なし
- フォロー：PSA を 1・3・6・9・12 か月で測定。12 か月目に確認の MRI を撮ってから監視生検
- 途中で PSA が上昇したら、まず MRI で再評価し、その結果を踏まえて患者と相談のうえ再生検または根治療法へ

**参考**
- GL：EAU 2026 は、低リスクと予後良好な中間リスクの一部（GG2）で監視療法を推奨。PSA の変化だけで積極的治療に移行しない

## 3. 限局癌の根治療法

**方針**
- RARP：切除可能と判断すれば施行
- リンパ節郭清：Briganti 2012 で 30% 以上なら拡大郭清
  - 施設基準。GL の 5% では対象症例が多くなりすぎ、国内の勤務時間の制約上運用できないため（他施設もおおむね 20% 前後）
  - 計算ツール：`tools/briganti2012.html`
- 放射線治療の ADT 併用
  - 予後不良な中間リスク：6 か月
  - 高リスク：2 年（6 か月先行し、RT 後に継続）
- 超高リスクへのアビラテロン追加：本来は行いたいが、国内では適応外のため行っていない

**参考**
- GL：EAU 2026 は、LNI リスクが Briganti 2012 で >5%、Briganti 2019 で >7% の場合に ePLND を推奨。超高リスク（cN1、または cT3-4・GS 8-10・PSA ≥40 のうち 2 つ以上）には ADT＋アビラテロン 2 年
- 根拠：[Briganti 2012（Eur Urol）](https://pubmed.ncbi.nlm.nih.gov/?term=Briganti+updated+nomogram+lymph+node+invasion+percentage+of+positive+cores+Eur+Urol+2012)、[STAMPEDE（非転移高リスクへのアビラテロン：Attard, Lancet 2022）](https://pubmed.ncbi.nlm.nih.gov/?term=Attard+abiraterone+high-risk+non-metastatic+prostate+cancer+STAMPEDE+meta-analysis+Lancet+2022)
- 保険適用：アビラテロンの「内分泌療法未治療のハイリスクの予後因子を有する前立腺癌」は LATITUDE（転移例）に基づく効能で、非転移例は適応外

> [!CAUTION]
> **Claude 提案（2026-11）**
> - 注視：アビラテロンの非転移高リスク例への国内適応拡大の有無
> - `tools/briganti2012.html` は原著の回帰係数が未登録で、まだ計算できない

## 4. 高リスク・局所進行

**方針**
- §3 に準じる（RARP の適応、高リスクでは ADT 2 年）

## 5. 術後 PSA 再発（BCR）

**方針**
- 断端陽性（RM1）：PSA 0.4 程度で救済放射線を検討。0.2 からの上昇の推移を確認したいため
- 病理が GG3 以上なら、救済放射線に ADT を併用
- 断端陰性（RM0）：画像で転移がなければ微小転移と判断し、まず ADT 単独で開始
- PSMA-PET は国内保険適用外のため使用しない

**参考：EAU の BCR リスク分類**

| | 低リスク BCR | 高リスク BCR |
|---|---|---|
| 前立腺全摘後 | PSA 倍加時間 >1 年 **かつ** pGG <4 | PSA 倍加時間 ≤1 年 **または** pGG 4-5 |
| 放射線治療後 | 再発までの期間 >18 か月 **かつ** 生検 GG <4 | 再発までの期間 ≤18 か月 **または** 生検 GG 4-5 |

- GL の考え方：低リスク BCR は経過観察（PSA モニタリング）も選択肢。高リスク BCR は早期救済放射線、必要に応じて ADT 併用。救済放射線は PSA 0.5 ng/mL 未満での開始を推奨
- 出典：[EAU BCR リスク分類（Van den Broeck, Eur Urol 2019）](https://pubmed.ncbi.nlm.nih.gov/?term=Van+den+Broeck+biochemical+recurrence+prostate+cancer+EAU+risk+groups+Eur+Urol+2019)、[2019 summary paper（全文 PDF）](https://eprints.whiterose.ac.uk/id/eprint/148704/3/EAU_PCA_GUIDELINES_BCR_FINAL%20summary%20paper%20April%202019.%20docx.pdf)、[北米コホートでの外部検証](https://www.citedrive.com/en/discovery/external-validation-of-the-european-association-of-urology-biochemical-recurrence-risk-groups-to-predict-mortality-after-radical-prostatectomy-or-radiation-therapy-in-a-north-american-cohort/)
- 救済放射線と ADT 併用の根拠：[RTOG 9601](https://pubmed.ncbi.nlm.nih.gov/?term=Shipley+radiation+with+or+without+antiandrogen+therapy+recurrent+prostate+cancer+NEJM+2017)、[GETUG-AFU 16](https://pubmed.ncbi.nlm.nih.gov/?term=Carrie+GETUG-AFU+16+salvage+radiotherapy+goserelin+Lancet+Oncol)、[SPPORT（NRG/RTOG 0534）](https://pubmed.ncbi.nlm.nih.gov/?term=Pollack+short-term+androgen+deprivation+pelvic+lymph+node+treatment+salvage+radiotherapy+SPPORT+Lancet+2022)
- 保険適用：ロカメッツ（68Ga-PSMA-11）はプルヴィクトの適応判定用。BCR の病期診断は適応外

> [!CAUTION]
> **Claude 提案（2026-11）：RM0 の BCR にすぐ ADT 単独で始める方針について**
> - EAU は BCR をリスクで分け、低リスクは経過観察も選択肢としている。ADT 単独の早期開始は全例には推奨されていない
> - 救済放射線は断端陰性でも有効とする報告がある。早期救済放射線の RCT のうち、[RADICALS-RT](https://pubmed.ncbi.nlm.nih.gov/?term=Parker+RADICALS-RT+timing+of+radiotherapy+after+radical+prostatectomy+Lancet+2020) と [RAVES](https://pubmed.ncbi.nlm.nih.gov/?term=Kneebone+RAVES+adjuvant+versus+early+salvage+radiotherapy+Lancet+Oncol+2020) は断端陰性（pT3 など）も含む。メタ解析は [ARTISTIC](https://pubmed.ncbi.nlm.nih.gov/?term=Vale+ARTISTIC+adjuvant+or+early+salvage+radiotherapy+meta-analysis+Lancet+2020)。断端の状態を含めた救済放射線の成績予測モデルは [Tendulkar（J Clin Oncol 2016）](https://pubmed.ncbi.nlm.nih.gov/?term=Tendulkar+contemporary+update+multi-institutional+predictive+nomogram+salvage+radiotherapy+J+Clin+Oncol+2016)
> - 高リスク BCR（PSA 倍加時間 ≤9 か月）では、[EMBARK](https://pubmed.ncbi.nlm.nih.gov/?term=Freedland+EMBARK+enzalutamide+leuprolide+biochemically+recurrent+prostate+cancer+NEJM+2023) でエンザルタミド（単独または＋リュープロレリン）が無転移生存期間を改善した。国内では適応外
> - 提案：RM0 でも EAU リスク分類で分け、低リスクは経過観察、高リスクは救済放射線±ADT を選択肢として提示する

## 6. nmCRPC

**方針**
- ダロルタミドから開始
- エンザルタミドは、タラゾパリブとの併用のために残しておく
- アビラテロン・エンザルタミド・アパルタミドは、化学療法・Lu-PSMA・Ra-223 を使い切った後に、さらに治療を希望する患者さんのために残しておく（交差耐性は理解したうえでの意図的な温存）

**参考**
- GL：PSA 倍加時間 ≤10 か月の nmCRPC には ARPI 3 剤いずれかを推奨（3 剤とも全生存期間を改善）。ARPI の後に別の ARPI へ切り替えることは推奨しない
- 根拠：[SPARTAN](https://pubmed.ncbi.nlm.nih.gov/?term=Smith+SPARTAN+apalutamide+nonmetastatic+castration-resistant+NEJM+2018)、[PROSPER](https://pubmed.ncbi.nlm.nih.gov/?term=Hussain+PROSPER+enzalutamide+nonmetastatic+castration-resistant+NEJM+2018)、[ARAMIS](https://pubmed.ncbi.nlm.nih.gov/?term=Fizazi+ARAMIS+darolutamide+nonmetastatic+castration-resistant+NEJM+2019)
- 保険適用：3 剤とも nmCRPC に適応あり
- 備考：ダロルタミドは中枢神経系の有害事象や転倒が少ない

## 7. mHSPC

**方針**
- 骨以外の臓器転移がなければ、基本は ADT＋ARPI
- トリプレット（ADT＋ARPI＋ドセタキセル）は、primary Gleason pattern 5 または臓器転移がある場合に考慮
  - CHAARTED の高腫瘍量だけでは基準として不十分と考える（GL との意図的な違い）
- 低腫瘍量・オリゴ転移への放射線（前立腺照射・MDT）は、PSA の推移と画像フォローの結果をみて判断

**参考**
- GL：EAU 2026 は、全身状態が保たれていれば全例に ADT＋ARPI を推奨。トリプレットはドセタキセルに耐えられる de novo 転移例、特に高腫瘍量に推奨。低腫瘍量の de novo 例には前立腺照射を推奨
- 根拠：[ARASENS](https://pubmed.ncbi.nlm.nih.gov/?term=Smith+ARASENS+darolutamide+docetaxel+metastatic+hormone-sensitive+NEJM+2022)、[PEACE-1](https://pubmed.ncbi.nlm.nih.gov/?term=Fizazi+PEACE-1+abiraterone+radiotherapy+de+novo+metastatic+castration-sensitive+Lancet+2022)、[CHAARTED](https://pubmed.ncbi.nlm.nih.gov/?term=Sweeney+CHAARTED+chemohormonal+therapy+metastatic+hormone-sensitive+NEJM+2015)、[STAMPEDE arm H（低腫瘍量への前立腺照射）](https://pubmed.ncbi.nlm.nih.gov/?term=Parker+STAMPEDE+radiotherapy+to+the+primary+tumour+newly+diagnosed+metastatic+prostate+cancer+Lancet+2018)
- 保険適用：ダロルタミドの mHSPC はドセタキセル併用で承認（2023 年）

> [!CAUTION]
> **Claude 提案（2026-11）**
> - 注視：[ARANOTE](https://pubmed.ncbi.nlm.nih.gov/?term=Saad+ARANOTE+darolutamide+androgen-deprivation+therapy+metastatic+hormone-sensitive+J+Clin+Oncol) に基づく ADT＋ダロルタミド（ドセタキセルなし）の国内適応追加の有無。2026 年 3 月に関連通知の報道があるが、内容は未確認

## 8. mCRPC

**方針**
- BRCA 検査は、mCRPC になりそうな時期に提出。myChoice を BRACAnalysis より優先
- BRCA 陽性：PARP 阻害薬を先に使う
- BRCA 陰性（ARPI 使用後の CRPC 1 次治療）：タラゾパリブ＋エンザルタミド、ドセタキセル、Lu-PSMA を提示して相談
- Lu-PSMA は、患者の希望があれば早めの時期に
- 画像で局所病変のみの場合は、RARP や放射線治療も考慮

**参考**
- GL：EAU 2026 は、転移性前立腺癌に生殖細胞系列の遺伝子検査を推奨し、腫瘍組織の HRR 検査も早めに考慮する
- 根拠：[PROfound](https://pubmed.ncbi.nlm.nih.gov/?term=de+Bono+PROfound+olaparib+metastatic+castration-resistant+NEJM+2020)、[PROpel](https://pubmed.ncbi.nlm.nih.gov/?term=Clarke+PROpel+abiraterone+olaparib+metastatic+castration-resistant+NEJM+Evidence)、[TALAPRO-2](https://pubmed.ncbi.nlm.nih.gov/?term=Agarwal+TALAPRO-2+talazoparib+enzalutamide+Lancet+2023)、[VISION](https://pubmed.ncbi.nlm.nih.gov/?term=Sartor+VISION+lutetium-177-PSMA-617+metastatic+castration-resistant+NEJM+2021)、[PSMAfore](https://pubmed.ncbi.nlm.nih.gov/?term=Morris+PSMAfore+177Lu-PSMA-617+taxane-naive+Lancet+2024)
- 保険適用
  - myChoice：腫瘍組織で BRCA1/2 と GIS を評価。CRPC で保険償還あり（[Myriad](https://investor.myriad.com/news-releases/news-release-detail/27171/)、[PMDA 添付文書](https://www.pmda.go.jp/PmdaSearch/bookSearch/01/14595057551023)）
  - タラゾパリブ＋エンザルタミド：2024 年 1 月に BRCA 変異陽性 mCRPC で承認。2026 年 3 月に HRR 変異の有無を問わない mCRPC へ拡大（[ケアネット](https://www.carenet.com/news/general/carenet/62540)、[PMDA](https://www.pmda.go.jp/PmdaSearch/iyakuDetail/GeneralList/4291081M1022)）
  - プルヴィクト（Lu-PSMA）：2025 年 9 月承認、11 月薬価収載。ロカメッツと同時承認（[Novartis](https://www.novartis.com/jp-ja/news/media-releases/prkk20250919)）
- 補足：myChoice は組織検査のため、体細胞変異か生殖細胞系列変異かを区別できない。陽性時は BRACAnalysis と遺伝カウンセリングで生殖細胞系列かどうかを確認する。保存検体が古いと検査に失敗しやすい

> [!CAUTION]
> **Claude 提案（2026-11）**
> - 注視：TALAPRO-2 は CRPC 1 次で ARPI 未治療の症例が中心。HSPC 期に ARPI を使った症例でのデータは限られる
> - 注視：Lu-PSMA を早めに使う場合は、国内添付文書の前治療要件（ARPI・タキサン）と、施設で PSMA-PET を撮れる体制かを確認

## 9. 骨関連事象・支持療法

**方針**
- ADT が 6 か月以上になる場合は骨密度を測定し、骨粗鬆症の危険域など必要があれば骨修飾薬を使う
- 骨転移への骨修飾薬は CRPC になるまで使わない

**参考**
- GL：ADT 中は骨折リスクを評価し、骨保護療法を行う。mHSPC での骨修飾薬に骨関連事象の予防効果はなく、使用は mCRPC の骨転移例で推奨（GL と一致）
- 根拠：[CALGB 90202](https://pubmed.ncbi.nlm.nih.gov/?term=Smith+CALGB+90202+zoledronic+acid+castration-sensitive+bone+metastases+J+Clin+Oncol+2014)、[デノスマブ vs ゾレドロン酸（Fizazi, Lancet 2011）](https://pubmed.ncbi.nlm.nih.gov/?term=Fizazi+denosumab+versus+zoledronic+acid+bone+metastases+castration-resistant+Lancet+2011)、[ERA 223](https://pubmed.ncbi.nlm.nih.gov/?term=Smith+ERA+223+radium-223+abiraterone+Lancet+Oncol+2019)
- 保険適用：デノスマブは骨転移にランマーク 120 mg、骨粗鬆症にプラリア 60 mg
- 備考：Ra-223 を使う場合は骨修飾薬の併用が推奨される（ERA 223 でアビラテロン併用時に骨折が増加）

---

## 改訂履歴

| 日付 | 変更点 | 根拠 |
|---|---|---|
| 2026-11 | 骨組み作成 | - |
| 2026-11-12 | 全セクションに方針を記入（聞き取り第 1〜4 回） | 聞き取り、EAU 2026 |
| 2026-11-12 | 表記を変更：方針（黒字）と Claude 提案（赤枠・リンク付き）に分離。§5 に EAU の BCR リスク分類と救済放射線の根拠を追加 | 聞き取り第 5 回 |
