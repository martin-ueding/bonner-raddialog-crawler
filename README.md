# Crawler für Bonner Rad-Dialog

Der [Bonner Rad-Dialog](https://www.raddialog.bonn.de/) lädt Bürger der Stadt
ein Verbesserungsvorschläge zur Radverkehrsführung einzureichen. Diese Daten
sind durchaus interessant, jedoch bietet die Seite keine Möglichkeit die
Rohdaten herunterzuladen. Für private Analysen oder als Kopie für später wäre
dies jedoch praktisch.

Dieses Skript lädt die öffentlichen HTML Seiten des Raddialogs herunter und
liest die Daten aus. Am Ende erhält man eine große [YAML](http://yaml.org/)
Datei, in der die Beiträge nach URL aufgeschlüsselt enthalten sind. Einer
meiner Beiträge sieht dann wie folgt aus:

    https://www.raddialog.bonn.de/dialoge/bonner-rad-dialog/schutzstreifen-im-tuerbereich-der-parkenden-autos:
      author: Martin Ueding
      comments:
      - answers: []
        author: Martin Ueding
        date: 23. Sep. 2017
        text: ["Ich glaube sogar, dass in Richtung Nord-Ost auf dem Boden ein blaues Symbol\
            \ ist, das ganze also als nutzungspflichtiger Radweg klassifiziert ist. Das\
            \ ist nat\xFCrlich blanker Hohn, wenn andererseits Gerichtsurteile Radfahrer\
            \ zu Abstand von parkenden Autos mahnen. ", "Was soll ich denn hier bitte\
            \ machen? Autofahrer \xFCberholen knapp, weil ihnen ja dank gestrichelter\
            \ Linie der Rest der Stra\xDFe geh\xF6rt ..."]
        time: '18:41'
        title: Nutzungspflichtig Richtung Nord-Ost?
      date: 21.09.2017
      lat: 50.727173
      lon: 7.081304
      next: https://www.raddialog.bonn.de/dialoge/bonner-rad-dialog/verengte-strasse-durch-parkende-autos
      text: ["Hier ist auf beiden Seiten ein \xBBSchutzstreifen\xAB, der direkt neben\
          \ den parkenden Autos herf\xE4hrt. M\xF6chte man hier, wie durch die Rechtssprechung\
          \ gefordert, hinreichend Abstand zu den Autot\xFCren halten, f\xE4hrt man au\xDF\
          erhalb des Schutzstreifens. Autofahrer \xFCberholen dann sehr knapp.", 'Entweder
          Schutzstreifen oder parkende Autos, aber nicht beides.']
      url: https://www.raddialog.bonn.de/dialoge/bonner-rad-dialog/schutzstreifen-im-tuerbereich-der-parkenden-autos
      votes: 1

Es gibt mehrere Absätze Text und es gibt einen Kommentar (auch von mir), der
aber keine Antworten enthält.

Diese YAML Datei kann man dann nach Belieben weiterverarbeiten.

## Nutzung der Daten

In den [Regeln des Rad-Dialogs](https://www.raddialog.bonn.de/regeln) steht zur
Lizenz der von Nutzern geschriebenen Beiträgen:

> 8. Lizenz und Urheberrecht
>
> Alle von den Teilnehmenden eingestellten Inhalte stehen unter der [CC
> by-Lizenz](https://creativecommons.org/licenses/by/4.0/), das heißt sie
> dürfen unter Nennung des (Nutzer-)Namens des Autors, sowie der URL der
> jeweiligen Seite auf dieser Plattform unentgeltlich weiter verwendet werden.
> Inhalte, zu deren Verwendung die Teilnehmenden im Rahmen dieses
> Online-Dialogs nicht berechtigt sind, dürfen nicht eingespeist werden. Die
> Teilnehmenden müssen selber prüfen, ob diese Berechtigung vorliegt.

Somit ist es also erlaubt, diese Daten herunterzuladen und wieder zu
veröffentlichen, solange die Namen der Nutzer erhalten bleiben.

Natürlich sollten diese Daten respektvoll genutzt werden.

## Abhängigkeiten

Das Skript braucht Python 3 und folgende Bibliotheken:

- `beautifulsoup` (HTML Parsing)
- `requests` (Herunterladen der Seiten)
- `yaml` (Ausgabeformat)

## Lizenz des Skripts

Das Skript ist unter der MIT/Expat Lizenz veröffentlicht.

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

<!-- vim: set spell spelllang=de tw=79 :-->
