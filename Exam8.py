
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS


poem = """Who rides so late through the windy night? The father holding his young son so tight.

The boy is cradled safe in his arm,
He holds him sure and he holds him warm.

Why is your face so frightened my son?

The King of elves, father, see him yon?

The Elfin King with his tail and crown?

It is the fog, my son, streaming down.

Yes, you my dear child, come go with me!

The games I play, you'll like them, come see.

The shore is coloured with flow'rs in bloom,
My mother's gold gowns, you will see soon.

Oh father, father, can you not hear
What the elfking promises? I fear!

Be calm, stay quiet my dearest son,
The wind blows the dry leaves of autumn.

My darling boy, won't you come with me?

I have daughters in whose care you'll be.

My daughters dance round the fairy ring.

Each night they'll cradle you, dance and sing.

Father, dear father, can you not see
The elf king's daughter staring at me?

My son, my son, I see it so well:
Gray meadows on which the moonlight fell.

I love you for your beauty of course,
If free you'll not come, I will use force.

Father, dear father, he's touching me.

Of elf king's hurt, father please, free me.

Dread grips the father, he spurs the roan,
In loving arms he feels the boy moan.

At last, the courtyard, with fear and dread,
He looks at the child; the boy is dead."""

poemGer = """Wer reitet so spät durch Nacht und Wind?
Es ist der Vater mit seinem Kind.
Er hat den Knaben wohl in dem Arm,
Er faßt ihn sicher, er hält ihn warm.

Mein Sohn, was birgst du so bang dein Gesicht?
Siehst Vater, du den Erlkönig nicht!
Den Erlenkönig mit Kron' und Schweif?
Mein Sohn, es ist ein Nebelstreif.

Du liebes Kind, komm geh' mit mir!
Gar schöne Spiele, spiel ich mit dir,
Manch bunte Blumen sind an dem Strand,
Meine Mutter hat manch gülden Gewand.

Mein Vater, mein Vater, und hörest du nicht,
Was Erlenkönig mir leise verspricht?
Sei ruhig, bleibe ruhig, mein Kind,
In dürren Blättern säuselt der Wind.

Willst feiner Knabe du mit mir geh'n?
Meine Töchter sollen dich warten schön,
Meine Töchter führen den nächtlichen Reihn
Sie wiegen und tanzen und singen dich ein.

Mein Vater, mein Vater, und siehst du nicht dort
Erlkönigs Töchter am düsteren Ort?
Mein Sohn, mein Sohn, ich seh'es genau:
Es scheinen die alten Weiden so grau.

Ich lieb dich, mich reizt deine schöne Gestalt,
Und bist du nicht willig, so brauch ich Gewalt!
Mein Vater, mein Vater, jetzt faßt er mich an,
Erlkönig hat mir ein Leids getan.

Dem Vater grauset's, er reitet geschwind,
Er hält in den Armen das ächzende Kind,
Erreicht den Hof mit Mühe und Not,
In seinen Armen das Kind war tot. """


print("Computing...")
tts = gTTS(text=poemGer, lang = 'de')
tts.save('poem.mp3')
tts = gTTS(text=poem, lang = 'en')
tts.save('poemEn.mp3')
#Please make sure to have ffmpeg successfully installed, otherwise the code will not function!!!
#See https://windowsloop.com/install-ffmpeg-windows-10/#download-ffmpeg for more information
poemAudio = AudioSegment.from_mp3("poemEn.mp3")
beatAudio = AudioSegment.from_mp3("beat.mp3")-15
mixed = poemAudio.overlay(beatAudio)
play(mixed)