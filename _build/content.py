# Site content, lifted from the existing denisflueraru.github.io pages.
# Image refs: "lh3:<id>" = Google-hosted image, anything else = file under media/.

CATS = {
    "art": ("Artwork", "art"),
    "ws": ("Workshop", "ws"),
    "col": ("Collab", "col"),
    "ex": ("Exhibition", "ex"),
    "snd": ("Sound", "snd"),
}

HB_TEXT = [
    "A modified medical stethoscope, fitted with an amplifier and a custom casing. "
    "The heartbeats it captures are passed through a distortion pedal and ultimately into a speaker.",
]

# ---------------------------------------------------------------- artworks
ARTWORKS = [
    dict(slug="heartbroken", title="Heartbroken", year="2026", new=True,
         hero="heartbroken/heartbroken-4.jpg", pair=["heartbroken/heartbroken-4.jpg", "heartbroken/heartbroken-3.jpg"],
         portrait=True,
         facts=[("Year", "2026"), ("Type", "Sound object"),
                ("Materials", "Modified medical stethoscope, amplifier, custom casing, distortion pedal, speaker")],
         text=HB_TEXT,
         gallery=["heartbroken/heartbroken-1.jpg", "heartbroken/heartbroken-2.jpg",
                  "heartbroken/heartbroken-3.jpg", "heartbroken/heartbroken-4.jpg"]),
    dict(slug="loopstudies", title="Loop Studies I–IV", year="2025", place="MAMŰ, Budapest",
         hero="lh3:1hnjBShd3nIb2AJuUqrQTyi_q4AZzpk--",
         facts=[("Year", "2025"), ("Type", "Ongoing series — sound, pen plots, surface imprints"),
                ("Shown at", "MAMŰ Társaság, Budapest")],
         text=[
             "Loop Studies is an ongoing series of works exploring the search for the perfect loop. Each piece is based "
             "on a 30-second musical loop created through a blend of analog and digital tools, combined with field recordings.",
             "The sound is then translated into a plotted drawing, where frequencies unfold into arcs and gestures. A surface "
             "imprint accompanies each plot, anchoring the loop in the physical world and connecting the sonic to the tactile.",
             "Sound visualisation generated in Processing from custom FFT analysis of recorded loops.",
         ],
         gallery=["lh3:1uRNN5-vI8pFjjcUf7SDuELM8gGhCujtV", "lh3:14j4oiF2yGQ8hyaAAsob5BfvhbxA6E_Z5",
                  "lh3:1WC96n2S3AWlTVplU7QR0GmOzabP0nr0O", "lh3:1btcyhnjH-Pci6qoH7KTpqG3BYU_6AjCI"],
         embeds=[("bandcamp", "696765584", "Listen to the loops — Loop Studies (I–IV)",
                  "https://denisflueraru.bandcamp.com/album/loop-studies-i-iv")]),
    dict(slug="beyondthenoisetheconcretespeaks", title="Beyond the noise, the concrete speaks", year="2024",
         place="WASP, Bucharest / Reduta, Brașov",
         hero="lh3:1iOGqVedeAODwo-r5t7_Zr2buzPIDGD4F",
         facts=[("Year", "2024 — 2025"), ("Type", "Casts and sound composition"),
                ("Editions", "Bucharest (2024), Brașov (2025)")],
         text=[
             "The series explores the urban milieu and turns the streetscape into a tactile journey through memory and place. "
             "The molds collectively resonate with the vibrant interplay between the city's history and contemporary experience, "
             "woven into a sound composition crafted from field recordings taken on location.",
         ],
         sections=[
             ("2025 — Brașov", ["lh3:1FXPJi129QXzYASn7aIac3H1B2QZKn6s5", "lh3:18BfKXSJEAqD303zcrI7mWk6x3l2J3uco",
                                "lh3:1Um6sHlKYFcIMfZ5jbzx97PUwCG_-xugy", "lh3:1Y7T6i5xPLjfxxIi6LjdXpXLN8FMONm-s"]),
             ("2024 — Bucharest", ["lh3:1fOrAwAmFtkqaAlY8dDSjzL_8fXPPFhA0", "lh3:1X6z1m5OAotd3GMsJxZsoMmUF135bXJ3N",
                                   "lh3:1v89Ulwdv1IKNFfMeIykVdtmAHZlHvl2S", "lh3:1Ssml8wZH7Y3G4U6xcCB3BiCqpKJNcFGU"]),
         ]),
    dict(slug="solara", title="Solara", year="2024", place="Fusion: AIR, /SAC Bucharest",
         hero="lh3:1FBcFT_MCZHQIbAU4boCs-gIm5JDvYek9",
         facts=[("Year", "2024"), ("Type", "Interactive installation"), ("Context", "Fusion: AIR residency, /SAC, Bucharest"),
                ("With", "Maximilian Teodorescu, Marius Echim — Institute for Space Science"),
                ("Tools", "Grasshopper, Rhino, Max MSP, custom EMF microphone")],
         text=[
             "During the Fusion Air Residency, I worked with two scientists from the Institute for Space Science, "
             "Maximilian Teodorescu and Marius Echim. Together, we built an interactive installation called Solara, "
             "which looks at the mixed relationship we have with the sun.",
             "I used Grasshopper and Rhino to design the voronoi structure of the installation, and Max MSP to create two sound pieces. "
             "Visitors explored the installation with a custom EMF microphone, scanning its surface to find “black spots” "
             "that revealed the dual nature of the sun — both life-giving and destructive.",
         ],
         gallery=["lh3:1rO_WEHru-ZoNiVBxeeCwcjm13oNbnvOR", "lh3:16K6ILZT43OdcKc0tlff2sk0oiG1kwW2t",
                  "lh3:1oOBUVf594GI2-E9PKUrfwK_-m8mOyTAn", "lh3:1CscSYGMS1w-ycOuc89Cr3IM-Yeiuv9Qf",
                  "lh3:1siwlv3Bioxq2XuNgusDNJ0m2JwNQ2K49"]),
    dict(slug="ruinedresonances", title="Ruined Resonances", year="2024", place="Thessaloniki",
         hero="lh3:1ZcHkWm3pe8xUKHgJ8L4jnNX4d8kIk8tX",
         facts=[("Year", "2024"), ("Type", "Object book series — field recordings and casts"),
                ("First edition", "Thessaloniki"), ("Support", "Culture Moves Europe")],
         text=[
             "A journey through sound and form. With the support of the Culture Moves Europe programme, Ruined Resonances broke "
             "boundaries for the first time, expanding our cross-modal archive with new locations.",
             "This object book series explores the memory of places through both sound and form. Each edition combines field "
             "recordings with gypsum molds taken from streets and landmarks. The book synthesizes each location’s acoustic signature "
             "with an alginate imprint, attempting to teleport readers into spaces layered with history, and highlight the contrast "
             "between past and present.",
             "As readers progress, they encounter casts that can be touched and recordings that can be listened to — deepening the "
             "connection to the site. The first edition was realized in Thessaloniki.",
         ],
         gallery=["lh3:1EbNRYpePm01JMMD7CYlFJUE1JBvg082S", "lh3:1O1LAKGMnxFpnuYJRA30ugimWqdEj2BwC",
                  "lh3:1tHDUAwA8YLC0zJJ6xi3GH2mZeASwsd7H", "lh3:1DVNSt1gzJha8haU8v-SJY3dA0LUbhdaY",
                  "lh3:1OuEtTt-WGSkKDldUgtS2AL7yaY78WMxl", "lh3:1Tpm2JwWNkdnrOAZ0ang-zVmtcmtI9ba1",
                  "lh3:1CiSTDxt81GKNNN6J2SMujJUfkAI74VAx", "lh3:1Aet-UwNQdRKdVa_ff3AtKvkt87osbxMH",
                  "lh3:114MkkOfqYeHOTcr0vco8ldFEc-b4sNoV"],
         embeds=[("bandcamp", "2960872114", "Listen — Thessaloniki",
                  "https://ruinedresonances.bandcamp.com/album/thessaloniki")]),
    dict(slug="metabloom", title="Metabloom", year="2023",
         hero="lh3:1_bJHf0ktjJWB7vWDhA4dr0N4gcSfrnaJ",
         facts=[("Year", "2023"), ("Type", "Installation — concrete, rusted steel, sound, light")],
         text=[
             "Metabloom takes the viewer into a dystopian world where humanity has built a mega-city, symbolized by a concrete mold "
             "encased in a rusted steel frame. The choice of materials reflects the dominance of urbanization and the suppression of nature.",
             "Standing in front of the piece, visitors hear a recurring grinding sound — the underground roots of resilient plants "
             "struggling to break through. These unseen plants are determined to reclaim their place in the chain of biodiversity. "
             "The sounds are paired with a pulsing light — a sign of life force and the unbreakable spirit of these hidden life forms.",
             "The installation invites reflection on the clash between the concrete jungle and resilient nature — a story about "
             "endurance, strength, and the unstoppable power of life itself.",
         ],
         gallery=["lh3:1yzNyw2wAtDxOg9-FuHmxebu0fIr1rJeF", "lh3:1PGj2HmNy3pXunBnD2V4cLKww-Zr8Q-4v",
                  "lh3:1sRT7AlpzwGIa5fvZI39zTdXQZHz05ZKd", "lh3:18gNyBhkNTsvzH3K27QnYLTiL910JsVGj"]),
    dict(slug="auraltopographies", title="Aural Topographies", year="2023",
         hero="lh3:1fY8qaE59XclLjimbn6npgNaU6RxAxkqH",
         facts=[("Year", "2023"), ("Type", "Interactive installation"),
                ("Related", "Texture Recording Tool (TRT) — MA thesis, UNATC")],
         text=[
             "Aural Topographies is an interactive installation that complements the Texture Recording Tool (TRT) and attempts to "
             "create a cross-modal experience by adding a physical dimension to the field recording domain.",
             "The audio recording process amplifies sound’s vibrations — taking off the invisible cloak that hides the compressions "
             "and decompressions of the medium, revealing the environment around us. The primary question that the TRT explores is "
             "how traditional field recordings can be expanded to include a new, “physical” sonic dimension.",
             "When listening to our surroundings, we form an image of the aural space but rarely consider how a tree bark, an old wall, "
             "or even the ground might sound. By using the principles of piezoelectricity, this project adds a tactile dimension to "
             "sound recording — amplifying textures themselves to create a form of “contact field recording.”",
         ],
         gallery=["lh3:1Tk-f4yQQj7gaopN2rwT7D-MMmHOYfqea", "lh3:1Gmlio-647p_4ORITnJ1TobmddErlL7YC",
                  "lh3:1uSCafQh2Aht3iYt71zESCRhV_u1uxyEA", "lh3:1r4_iPD9qnUgHvoSArjD96DK6haeU8Rmt",
                  "lh3:10nnY8vT-RHYVyG_FxXC0S3zOzvZA-vUv", "lh3:1vF1A3SYli4bJaw6G-5BX2omKtol-qJYu",
                  "lh3:1SB0TekUuOmRxnIdBIQDcXOPXJAcCzjT0"],
         embeds=[("youtube", "xqloFNLGhyw", "About the work", None)]),
    dict(slug="interstatic", title="Interstatic", year="2023",
         hero="lh3:1l1tfGEDosWAcByBx9vNqN6L-MH76H77R",
         facts=[("Year", "2023"), ("Type", "Interactive installation"),
                ("Built from", "VEF 202 radio (USSR), Western microphone, motorised tuner"),
                ("Tools", "Max MSP, machine-learning voice recognition")],
         text=[
             "Interstatic is an interactive installation built from a VEF 202 radio made in the USSR and a Western microphone, "
             "hacked together to tell the story of the Cold War through the language of media. The work explores how news and "
             "propaganda shaped perception during this tense period, using sound as the main storyteller.",
             "Divided into six phases, each one reveals a different aspect of the Cold War. When the user speaks a letter from the "
             "callsign, they trigger a corresponding broadcast. Using Max MSP and a machine learning algorithm, the installation "
             "recognizes voice input and drives a motorized tuner that searches and clicks between frequencies.",
             "The result is a powerful sensory experience that merges vintage technology with modern hacking, inviting the audience "
             "to engage directly with the media tensions of the time.",
         ],
         gallery=["lh3:1AFUz99881mNUWJobufAnmosEbuzmsV7l", "lh3:1Q_DCOaK78QG5sW_5HNVZgTh5OOLLH_mH",
                  "lh3:1fJqA5bFM9ew9IiQs68e6H5_AvrCZKWgJ"],
         embeds=[("youtube", "GVKlL0fKzGo", "How the installation works", None)]),
    dict(slug="particlecomposer", title="Particle Composer", year="2022", place="Spotlight Festival, Bucharest",
         hero="lh3:13gRLmgU4Cc_zzZ3QkX-EqgVkzqpqUUMi",
         facts=[("Year", "2022"), ("Type", "Interactive installation — air-quality sensor, generative music"),
                ("Shown at", "Spotlight Festival, Bucharest")],
         text=[
             "While air pollution is drastically increasing due to our heavier carbon footprint, particle matter has turned into a "
             "“silent killer” that crosses all borders, posing a severe health threat and a significant decrease in life expectancy. "
             "PM 2.5 is responsible for an estimated 4.2 million premature deaths every year globally.",
             "The installation uses an air quality sensor to measure the concentration of particles in the air and, based on that, "
             "creates music that gets distorted and changes its harmony. The newly formed “continents” you can see on the globe are "
             "pollution particles seen under a microscope.",
         ],
         gallery=["lh3:15pqLNIIj1MF5G2fc_nwtkXrhWCKEYMg1", "lh3:1xyUBLOWNYVTOZ9OmI6QrxW3St5_pGTCI",
                  "lh3:1qgKZxGdv8MfRdwcLXXKJnQ_sxfr975XR",
                  "lh3:1203-v0OgsQm26Vrdr9jXe2ctePflxMUk"]),
    dict(slug="inversesurveillance", title="Inverse: Surveillance", year="2022",
         hero="lh3:1GTc6OVUJEUJd4OnZlNg-XlHI_k174LR5",
         facts=[("Year", "2022"), ("Type", "Interactive installation — human-scale CCTV")],
         text=[
             "Inverse:Surveillance is an interactive installation that explores panopticism and the act of sousveillance. "
             "The work takes the form of a human-scale CCTV, allowing participants to look back at systems of power.",
             "The installation reflects on algorithmic authority, the loss of privacy, and how control systems are reinforced by our "
             "own actions. Visitors grab the CCTV antenna and peer through its eye to uncover what lies behind surveillance.",
         ],
         gallery=["lh3:1achp2irmrqsm0DSUSEBMj5LA8dmM46Qv", "lh3:1gstR_F4iAkUsTS3DS6aCHHWubqceqFlr",
                  "lh3:1UC03WpDAwZPqBG1VqPO5qknEIdradvf7", "lh3:182yiTLhqyX4Gc4P7mCkm2DZcDuoC4B-c"]),
    dict(slug="rewind", title="Rewind", year="2022",
         hero="lh3:1klWq7A-0sP7v82HJq6t7Hd8EOnrUKJIB",
         facts=[("Year", "2022"), ("Type", "Interactive audio installation"),
                ("With", "Alexandru Berceanu"), ("Exhibition", "White Imprint")],
         text=[
             "An interactive audio installation in collaboration with Alexandru Berceanu, part of the White Imprint exhibition.",
             "In a striking resolution in 2022, the Supreme Court decision in Roe vs. Wade was overruled, reopening the possibility "
             "for states to prosecute medical personnel for performing abortion procedures.",
             "In Rewind, a bot reads fragments of the 1973 Supreme Court decision, gradually fading into the 2022 ruling. Two tape "
             "recorders loop the recordings, continuously transferring and degrading the message. The installation is triggered by a "
             "proximity sensor.",
         ],
         gallery=["lh3:1CN0nhgbHY8A98LXiZroMTLNAH95CzrTh", "lh3:1UBkQDfHo7oQ1U-lghe3HvkC_cmJO6fpe",
                  "lh3:1vWDf67aY3DZn5nYyyJaRZgx_O6FPdvmG"],
         embeds=[("short", "YWn-q_v3gDM", "Video", None)]),
]

# ---------------------------------------------------------------- workshops
WORKSHOPS = [
    dict(id="sensors-haptics", title="Sensors & Haptics for Performative Arts", year="2025",
         place="NOD Makerspace, Bucharest",
         text="Participants learned how to build a glove-like wearable interface that uses sensors to modify sound in real time, "
              "translating gesture and motion directly into audio transformation.",
         main="lh3:1cFurzbAfnNpt9pkafrv_zAZltE5o2hqH",
         grid=["lh3:1OVS34sKvNcsC-WaE5HHnjnTyVli5vW-K", "lh3:1IJH2SvALRKdv673TZ5vRIiCvcGcY2WNV",
               "lh3:1eWHYJr0uoKeyjcgVQLGBxtYVN4egkKaL", "lh3:1SaIVT4q6wYCbkUbaJ1U3nBeB165BOHu7"]),
    dict(id="start-pentru-tineri", title="Start Pentru Tineri", year="2025", place="subStejar, Târgu Lăpuș",
         text="Children from Târgu Lăpuș, Maramureș learned how to build two types of microphones, EMF and contact microphones. "
              "By collecting hidden and overlooked sounds from their surroundings, participants later composed a collective audio "
              "piece, transforming the subStejar location into a collaborative audio piece.",
         main="lh3:1LtRd_qzufJse31q3usaBv5ZzEiNonHJZ",
         grid=["lh3:18RhxgisUs67RyLweUklO78oW8jpfCiRr", "lh3:1QQM5Q55UbHBF_6Qt2lxbh7sftempWrYu",
               "lh3:1c1e9ZKZmCxEXw5KGy7daSa7z2gKYVe4F", "lh3:1-MPJ-kT2ub7O5KL7J3Ah3X0CSrYXrTUi"]),
    dict(id="contact-mics-preamps", title="Contact Mics & Preamps", year="2025", place="CAV Gallery, Bucharest",
         text="Participants built DIY microphones together with preamps and explored recording techniques, later composing "
              "textures and rhythms in Ableton Live.",
         main="workshops/cavmainpost.jpg",
         grid=["workshops/cav1.jpg", "workshops/cav2.jpg", "workshops/cav3.jpg", "workshops/cavmain.jpg"]),
    dict(id="recycle-your-technology", title="Recycle Your Technology", year="2024",
         place="Bucharest, Arad, Reșița, Brașov",
         text="A hands-on workshop where participants soldered and assembled electromagnetic microphones, then used them to capture "
              "electromagnetic rhythms in the gallery space. It later evolved into a series across Romania, where participants from "
              "different cities learned how to build microphones and explore local soundscapes.",
         main="workshops/r9_main.jpg",
         grid=["workshops/ryt_b_3.jpg", "workshops/ryt_b_4.jpg", "workshops/ryt_bv2.jpg", "workshops/resita3.jpg",
               "workshops/resita1.jpg", "workshops/resita2.jpg", "workshops/ryt_arad.jpg", "workshops/ryt_bv3.jpg"]),
    dict(id="nova", title="Contact Microphones & Composition", year="2023", place="NOVA Festival, Bucharest",
         text="We explored the urban environment with microphones, creating a sonic map of the city and later transformed the "
              "sounds into a collaborative composition.",
         main="workshops/nova-main.jpg",
         grid=["workshops/nova_1.jpg", "workshops/nova_2.jpg", "workshops/nova_3.jpg", "workshops/nova_4.jpg"],
         video="dJfU8wuCUzI"),
    dict(id="sonic-explorations", title="Sonic Explorations — Pixels From a Future Past", year="2023",
         place="National Museum of Contemporary Art (MNAC), Bucharest",
         text="The pilot musique concrète workshop, where participants learned the foundation elements of experimental music and "
              "built their first contact microphone, later creating a collaborative composition in Ableton Live.",
         main="workshops/mnac1.jpg",
         grid=["workshops/mnac2.jpg", "workshops/mnac3.jpg", "workshops/mnac4.jpg", "workshops/mnac5.jpg"]),
]

# ---------------------------------------------------------------- collabs
COLLABS = [
    dict(id="caprices", title="Caprices Festival", year="2026", place="Gstaad, CH",
         text="Part of the production team for Sergiu Doroftei's light installations for both Peak and Ridge stages.",
         main="lh3:1aZWsn_scc48egopfl5gqAGmxJolSzu0e",
         grid=["lh3:1GDtWfMIZUTAeJXuPVHBchcrKKuIE_I8e",
               "lh3:1UaUuoPS06CLtYfYY0nkC_pUI3gGSEGfw", "lh3:14oeMzAfQDgw2KflSM1wVbJjoc9uY5Hea"]),
    dict(id="hush-glitches", title="Hush Glitches", year="2025", place="National Dance College, Bucharest",
         text="Developed within a larger multidisciplinary team in collaboration with the Bucharest Institute of Biology, this "
              "performance explored the relationship between body, environment, and digital media. I designed a sensor-rigged shoe "
              "integrating humidity, temperature, pressure, and light sensors, enabling dancers to influence sound and video content "
              "in real time.",
         main="lh3:1x8O-HLavFb0hcv_ufYeuEPb_gMrPIIxY",
         grid=["lh3:1Ad460EW2CeIpUMo2Ugt3y237MzFsLXjU", "lh3:1r2BdbkQv_1nBWX2V-E9qiWMEQNNul1ot",
               "lh3:1c1vksvZCEmJu4RB_PrE0Gm3iwxPnTNjG", "lh3:1mxMMkL_k-_O8mig2klhLpB2K45QFbjB9"]),
    dict(id="yokogawa", title="Yokogawa — Fresh Water Generator", year="2025", place="FabLab Bucharest",
         text="LED installation and programming of five distinct animation states, complemented by sound design for a dynamic "
              "technical presentation.",
         main="lh3:1MHFCQ-KB6U12IwIGFWT-LqtEa5l6kZkO",
         grid=["lh3:1Ga83g032iMIwce7BYzUIeLMvNoNE--mW", "lh3:1wCdb0xtbB1B4bvHSGPUV9XaIzANif8Pk",
               "lh3:14rdTCidSeR7UMpObFf4XtD0ZBGxBE9VF", "lh3:1YvOfAqHAah-uM2ToCw9yAy60SOcHxUWi"]),
    dict(id="artists-play-with-time", title="Artists Play with Time", year="2025", place="Performances across the EU",
         text="A series of bespoke contact microphones and preamp boxes designed to amplify the subtle ticking of clocks as "
              "instruments for performers. From 3D modeling and printing to soldering, shielding, and sound testing — every detail "
              "was tuned to bring time into focus.",
         video="It5iu3jE_kM"),
    dict(id="iqos", title="Echoes of Presence × IQOS", year="2024", place="Romanian Design Week, Bucharest",
         text="Creation of the complete sound environment across three interconnected rooms, where visitor movement dynamically "
              "triggered and shaped spatial audio.",
         main="lh3:1OatSKFv22k8QY7MsGcR9i-4BnvksaOFh",
         grid=["lh3:15w2rN46hEq9N4_WnK9LSLZ4M-IURg1xF", "lh3:1Fvz2ECaf9--dDPJfssIbFM4RnrLtp3Sa",
               "lh3:187ao1ubFxbMfAqbBDvInHj04i5JAlCmi", "lh3:1vN5LZSgsPu2It-78cB7kg1bNQ7ZdVXfh"]),
    dict(id="eon", title="E-ON Frosted Waves — Electric Castle", year="2024", place="Rizi Design, Cluj-Napoca",
         text="Sound design for a large-scale LED scenography installation. Creative direction: Alina Rizescu & Bogdan Stefanescu.",
         main="lh3:1uNKWTmCn9LdThl8it4Fdid8PAJ017737",
         grid=["lh3:1OpOq-fjR1CawgMp69qOB3qwVz2a1l6fi", "lh3:1UOVyb8DnNwV7PadqB44oj7b4BRtYJ-lB",
               "lh3:1RkmThQHUOcwLOmg-8uYKGOREEJ5SuRGA"]),
    dict(id="divaircity", title="DivAirCity Bucharest", year="2024", place="Piațeta Italiană, Bucharest",
         text="Generative drawing and air-quality visualizations.",
         main="lh3:1kkEK05SAhgmLcNOA7-VFuZptQG-hGf4N", grid=[]),
    dict(id="nos-utopies", title="Nos Utopies", year="2022", place="Fête des Lumières × Goethe-Institut, Lyon",
         text="Interactive performance connecting performers worldwide. I developed a machine-learning-driven system influencing "
              "the sound ensemble and performed the musical composition live.",
         main="lh3:1n2eSmJwzC9o8TSeLZ0A_uUemEMX3omP9",
         grid=["lh3:1-UzeeOrRF_ut6qEJOGcIUw95p5nhODHT", "lh3:1cf6H_dcBlWFQ24wXc2ccI66EptgnKJeP",
               "lh3:14F2CexeOlSqxtB7zuA4DG15azj3_GeHc", "lh3:1QcddbnBbws6ze_LjqIf-Uq5cT10QZOJP"]),
]

# ---------------------------------------------------------------- exhibitions
EXHIBITIONS = [
    dict(id="horizont-2", place="MAMŰ Társaság, Budapest", title="A Horizont Lényege II", year="2025",
         dates=["November 7 – November 28, MAMŰ Társaság, Budapest, HU"],
         imgs=["1vN3wlfUw4dhy41UIGbQipyyTEaGpuQe9", "1mpPLuPYjQeycvFg_yTtW-cS7bFJprv73", "1HEGJ0PUe0-yfMoM1jx__lzlP2zPaeGz2",
               "1uR9ZzANRr1IvxCKJaWiTQf6lwv-ysjbe", "1olvdpTB94IlYkPV1zCCYeFEt_KAt2MPa", "15YRtDi0rT_M6TdaJrArz-sb0AaHsdTiz"]),
    dict(id="main-point", place="Reduta Cultural Centre, Brașov", title="The Main Point of the Horizon", year="2025",
         dates=["April 8 – April 28, Cultural Centre Reduta, Brașov, RO"],
         imgs=["1UngB1DGX1qiKS3YfFD6fMhegsXAEA4sd", "1xhbcZRHWSCylVuMMuxWFLDnczQCMku2q", "1iaZrxj2f9RSBLs-YjLIjtQgAZSbBWiSW",
               "1ZR-TkHW2nj_a-RffhoPxGMCuaGAOW7sW", "1ZBQpxn8CCIcf4bp7icDh9oQYW2VeBUdm", "1sTM3O6V6TaaLNhDa5rb3cg_qooRowW5f"]),
    dict(id="unbound-echoes", place="WASP Studio, Bucharest", title="Unbound Echoes", year="2024",
         dates=["November 11 – November 24, WASP Studio, Bucharest, RO"],
         imgs=["1YBjprrQEOX5krHQmuYQpxZa7A8NswcEP", "1rlsJ-RgRMkRv5r48_yi9ZCfO36OX_DeN", "1GkrMP_G2uk5x5tGFJOJcfJNfqpmb1Ups",
               "1MX6FRimjStYrMqy-uvWj_OpnWyD_nPWR", "1lJOx4jILv9ZfrHvzoDnmKwxVziEncu68", "1M_7Sqe8KfgzFwEZxUVsqC5kFcnrkvY4L"]),
    dict(id="fusion-air", place="/SAC, Bucharest", title="Fusion: AIR", year="2024",
         dates=["September 17 – October 12, /SAC, Bucharest, RO"],
         imgs=["1qw7xHoC1uZCagizpYx85DVgYAeIl2vyO", "1_Nl0PcW9AsNkEhovDwL2IsS9nt4QqMva", "1zw4v1kKucst6edQ0liKZi8io3eafoS-v",
               "1ntMQLQ3Gwr19WljYjFjHbc2F4rBCqyoe", "1Bh4vcrz3zgvEyKdqDTlF3d_4P9VJi8-Y", "1aNFCr_fW_ivXR78frfs3IBn8SVUMpmyS"]),
    dict(id="recycle-your-technology", place="Reșița, Arad, Brașov, Bucharest", title="Recycle Your Technology", year="2024",
         dates=["May 18 — Salonul de Artă și Industrie, Reșița, RO", "June 21 — Museum of Arts, Arad, RO",
                "August 30 — Centrul Multicultural, Brașov, RO", "October 25 — Rezidența 9, Bucharest, RO"],
         imgs=["1wDNAtbhVGD-68tYDFg8rVqxoxk5DACzH", "1uOahHKIPcqNVdf1DaUgMRp75AuJVjV9M", "1iReeKkbggVGcojD1RNpvoHr9GZIohSFS",
               "1R-WvzuAnI1ENzx5Hr7xcaPuFjWMzbRwT", "1ByRvm7mBT0uRQwoSouGbVVSuXiDdV3cx", "1UVbp_shVUbqYvFv5K_csXZuGS6qOuiHd"]),
    dict(id="gelato-machine", place="Museum of Art, Brașov", title="Fabulating About a Gelato Machine", year="2023",
         dates=["November 10, 2023 – February 25, 2024, Museum of Art, Brașov, RO"],
         imgs=["1aS_XelrdGMOKaU6btoq44vFParVuTSHb", "1uFWscQYNEI7P8zrgUrpkY3qyZgUVW5GO", "1akzO-kMoWs4gfdgPR17GDaLI6eQ4UMq_",
               "1d0jScBDJ6ZS6F5ggh-TctWv4Is-qVd6r", "1F1-qRpNdfw_xlZgFMYFUuH1xGkoM8-UF", "1oiJ-QVkpnip0xMcQ85nLiWIsWGBRoDJP"]),
    dict(id="radar", place="Magazinul București", title="RADAR", year="2023",
         dates=["October 27 – October 29, Magazinul București, RO"],
         imgs=["1oFVrD4qtKl0OPYSM-bvy_YEjFot2Z6Dq", "1zJ5KMfgRKCLSJ8je_Hs4MDW81fpb_S85", "1bweGjt5hxL6fLFzYQa4FdVwvH5NYe0P2",
               "1zPsEbi3-7jvTbOf0x7kqWDzoZn6rISag", "1Y-HEdxkBIoMNv8-r_GWjpkME5lqYMUHZ", "1UqLbs0AP5pb0l1UJ82Fmz4ng6M17P2pA"]),
    dict(id="unliving-gallery", place="WASP, Bucharest", title="Un/Living Gallery: A Tangible Art Manifesto", year="2023",
         dates=["August 16 – October 12, WASP, Bucharest, RO"],
         imgs=["1zvNzTOBByMV0Qjjgni2NrwgSvP0Ef0hf", "1cKVGW1l9QkFtK2zRSyCFjfigDwAObKyY", "1K-WfVR0BSNih6loozRfXL55bcSfec8id",
               "1EYTivBF1INVuhu8dKaxKTLf-0BfYkl3B", "1U4VUUEVdYCg0-7dHsok7yUNbzypkJb_c", "1yH1roe8QwsbBu3-IYEn0RsGmV5K7AJCf"]),
]

# ---------------------------------------------------------------- index (home)
# (title, year, cat, place, href)
def _index():
    rows = []
    for a in ARTWORKS:
        rows.append((a["title"], a["year"], "art", a.get("place") or dict(a["facts"])["Type"].split(" — ")[0], f'{a["slug"]}.html'))
    for w in WORKSHOPS:
        rows.append((w["title"], w["year"], "ws", w["place"], f'workshops.html#{w["id"]}'))
    for c in COLLABS:
        rows.append((c["title"], c["year"], "col", c["place"], f'collabs.html#{c["id"]}'))
    for e in EXHIBITIONS:
        place = e["place"]
        rows.append((e["title"], e["year"], "ex", place, f'exhibitions.html#{e["id"]}'))
    rows += [
        ("Unul Dintre Noi — theatre sound design", "2024", "snd", "Teatrul de Comedie, Bucharest", "sound.html"),
        ("LESEL — OT001 EP", "2024", "snd", "Music release", "sound.html#lesel"),
        ("FIELD5 — phantom-powered contact microphone", "2025", "snd", "ATOMAT LAB", "https://atomatlab.com"),
        ("ERT01 — electromagnetic microphone", "2023", "snd", "ATOMAT LAB", "https://atomatlab.com"),
    ]
    order = {"art": 0, "col": 1, "ex": 2, "ws": 3, "snd": 4}
    rows.sort(key=lambda r: (-int(r[1]), order[r[2]]))
    # keep Heartbroken first
    rows.sort(key=lambda r: r[0] != "Heartbroken")
    return rows

INDEX = _index()

SERVICES = [
    ("Sound Design & Composition",
     "Immersive soundscapes, field recordings and generative audio for installations, performances and bespoke compositions. "
     "Audio is crafted with analog media such as tape and organic recordings, and with digital tools, integrating MIDI and live "
     "interaction systems driven by human and non-human controllers — buttons, sensors and other interfaces. Voiceovers and "
     "post-production for podcasts, films, jingles, commercials and music, alongside live performances, workshops and audio "
     "repair. Further explorations use contact microphones, electromagnetic sensors and custom instruments.",
     ["Ableton Live", "Pro Tools", "Max MSP", "Field recording", "Voiceover", "Post-production", "Custom instruments"]),
    ("Interactive & Software Development",
     "Dynamic interactive experiences built through software development, sensor integration and generative algorithms, "
     "with machine-learning interfaces for human recognition, gesture and environmental interaction. Projects span responsive "
     "installations, interactive performances and experimental systems, with a focus on real-time audio-visual feedback and "
     "immersive engagement.",
     ["C", "JavaScript", "Processing", "Arduino", "Max MSP", "Machine learning", "Sensors"]),
    ("3D Design & Fabrication",
     "Models are created digitally for visualisation, planning and production. Physical prototypes and installations are "
     "realised through 3D printing, laser cutting, CNC machining and hands-on craftsmanship, then painted and finished so the "
     "conceptual, technical and aesthetic sides come together.",
     ["Rhinoceros 3D", "Blender", "3D printing", "Laser cutting", "CNC", "Finishing"]),
    ("Creative & Project Development",
     "Ideas are turned into tangible projects through sketching, research and iterative brainstorming, aligned with the "
     "client’s goals or the project’s objectives. Structured planning balances conceptual exploration with practical execution, "
     "and collaboration keeps projects moving from initial vision to realised outcome.",
     ["Concept", "Research", "Planning", "EU-funded project coordination", "Teamwork"]),
]
