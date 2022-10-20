<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <link rel="icon" href="https://te.legra.ph/file/605e03714ef7a5cab09e3.jpg" />
    <meta name="title" content="amoremods">
    <meta name="description" content="Amore Modules">

    <meta property="og:type" content="website">
    <meta property="og:title" content="amoremods">
    <meta property="og:description" content="Amore Modules">
    <meta property="og:image" content="https://te.legra.ph/file/605e03714ef7a5cab09e3.jpg">

    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="amoremods">
    <meta property="twitter:description" content="Amore Modules">
    <meta property="twitter:image" content="https://te.legra.ph/file/605e03714ef7a5cab09e3.jpg">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AmoreMods</title>
    <style type="text/css">
        @import url('https://fonts.googleapis.com/css2?family=Consolas&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans');
        @import url('https://fonts.googleapis.com/css?family=Orbitron&display=swap');
        @import url('https://fonts.googleapis.com/css?family=Hind&display=swap');
        * {
            box-sizing: border-box;
        }
        
        body {
            width: 100%;
            height: 100%;
            margin: 2;
            padding: 0;
            background-color: rgb(89, 255, 0);
            font-family: Consolas, Monaco, 'Andale Mono', monospace;
            font-size: 16px;
            padding: 50px;
        }
        
        .mods {
            text-align: center;
            padding: 50px;
        }
        
        .mod {
            border: 1px solid rgba(255, 0, 0, 0.1);
            border-radius: 10px;
            padding: 5px 10px;
            display: inline-block;
            margin: 5px 5px;
            user-select: none;
            cursor: pointer;
            transition: all .3s ease;
            background: rgba(0, 255, 145, 0.19);
            position: relative;
            color: rgb(0, 0, 0);
            font-size: 13px;
        }
        
        @keyframes fadein {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        @keyframes fadeout {
            from {
                opacity: 1;
            }
            to {
                opacity: 0;
            }
        }
        
        .flex {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .title {
            font-size: 16px;
            color: #a9b7c6;
            text-decoration: none;
        }
        
        .icon {
            height: 20px;
            margin: 0 5px;
            animation: fadein .90s ease-out forwards;
            opacity: 100;
        }
        
         ::-webkit-scrollbar {
            width: 8px;
            background: #303841;
            height: 8px;
        }
        
         ::-webkit-scrollbar-track {
            background: #444b53;
            border-radius: 3px;
        }
        
         ::-webkit-scrollbar-button {
            display: none;
        }
        
         ::-webkit-scrollbar-corner {
            background: #303841
        }
        
         ::-webkit-scrollbar-thumb {
            background: #696f75;
            border-radius: 3px;
        }
        
        @media screen and (max-width: 736px) {
            body {
                padding: 20px;
            }
            .title {
                font-size: 14px;
            }
            .icon {
                height: 24px;
            }
        }
        
        .hidden:before {
            z-index: 100;
            content: '';
            display: block;
            width: 100%;
            height: 30px;
            position: absolute;
            background: rgba(0, 0, 0, .4);
            padding: 100px;
            margin-top: -50px;
            margin-left: -50px;
            /*animation: fadeout .15s ease-out forwards;*/
        }
        
        .hidden {
            overflow: hidden;
        }
        
        .selected {
            border: 2px solid #efefef;
        }
        
        * {
            border: 0;
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
         :root {
            --bg: #e3e4e8;
            --fg: #17181c;
            --input: #ffffff;
            --primary: #255ff4;
            --dur: 1s;
            font-size: calc(16px + (24 - 16)*(100vw - 320px)/(1280 - 320));
        }
        
        body,
        input {
            color: var(--fg);
            font: 1em/1.5 Hind, sans-serif;
        }
        
        form,
        input,
        .caret {
            margin: auto;
        }
        
        form {
            position: relative;
            width: 100%;
            max-width: 17em;
        }
        
        input,
        .caret {
            display: block;
            transition: all calc(var(--dur) * 0.5) linear;
        }
        
        input {
            background: transparent;
            border-radius: 50%;
            box-shadow: 0 0 0 0.25em inset;
            caret-color: var(--primary);
            width: 2em;
            height: 2em;
            -webkit-appearance: none;
            -moz-appearance: none;
            appearance: none;
        }
        
        input:focus,
        input:valid {
            background: var(--input);
            border-radius: 0.25em;
            box-shadow: none;
            padding: 0.75em 1em;
            transition-duration: calc(var(--dur) * 0.25);
            transition-delay: calc(var(--dur) * 0.25);
            width: 100%;
            height: 3em;
        }
        
        input:focus {
            animation: showCaret var(--dur) steps(1);
            outline: transparent;
        }
        
        input:focus+.caret,
        input:valid+.caret {
            animation: handleToCaret var(--dur) linear;
            background: transparent;
            width: 1px;
            height: 1.5em;
            transform: translate(0, -1em) rotate(-180deg) translate(7.5em, -0.25em);
        }
        
        input::-webkit-search-decoration {
            -webkit-appearance: none;
        }
        
        label {
            color: #e3e4e8;
            overflow: hidden;
            position: absolute;
            width: 0;
            height: 0;
        }
        
        .caret {
            background: currentColor;
            border-radius: 0 0 0.125em 0.125em;
            margin-bottom: -0.6em;
            width: 0.25em;
            height: 1em;
            transform: translate(0, -1em) rotate(-45deg) translate(0, 0.875em);
            transform-origin: 50% 0;
        }
        
        @media (prefers-color-scheme: dark) {
             :root {
                --bg: #e3e4e8;
                --fg: #ffffff;
                --input: #0000003a;
                --primary: #303841;
            }
        }
        /* Animations */
        
        @keyframes showCaret {
            from {
                caret-color: transparent;
            }
            to {
                caret-color: var(--primary);
            }
        }
        
        @keyframes handleToCaret {
            from {
                background: currentColor;
                width: 0.25em;
                height: 1em;
                transform: translate(0, -1em) rotate(-45deg) translate(0, 0.875em);
                opacity: 0;
            }
            25% {
                background: currentColor;
                width: 0.25em;
                height: 1em;
                transform: translate(0, -1em) rotate(-180deg) translate(0, 0.875em);
            }
            50%,
            62.5% {
                background: var(--primary);
                width: 1px;
                height: 1.5em;
                transform: translate(0, -1em) rotate(-180deg) translate(7.5em, 2.5em);
            }
            75%,
            99% {
                background: var(--primary);
                width: 1px;
                height: 1.5em;
                transform: translate(0, -1em) rotate(-180deg) translate(7.5em, -0.25em);
            }
            87.5% {
                background: var(--primary);
                width: 1px;
                height: 1.5em;
                transform: translate(0, -1em) rotate(-180deg) translate(7.5em, 0.125em);
            }
            to {
                background: transparent;
                width: 1px;
                height: 1.5em;
                transform: translate(0, -1em) rotate(-180deg) translate(7.5em, -0.25em);
            }
        }
        
        .mod:before {
            content: '';
            display: block;
            width: 100%;
            height: 100%;
            z-index: 10;
            position: absolute;
            margin-left: -10px;
            margin-top: -10px;
            padding-right: 10px;
            padding-bottom: 10px;
        }
        
        .invisible {
            animation: fadeout .15s ease-out forwards;
        }
        
        .mod_window {
            min-height: 150px;
            padding: 10px;
            width: 300px;
            border: 1px solid rgba(255, 0, 0, 0.1);
            background: rgba(0, 0, 0, 0.398);
            left: 0;
            top: 0;
            position: absolute;
            border-radius: 15px;
            display: none;
            transition: margin .3s ease;
            z-index: 100;
        }
        
        .mod_description {
            color: #ccc;
            padding: 10px;
            text-align: center;
            font-family: Consolas;
            user-select: none;
            font-size: 15px;
        }
        
        .inline {
            user-select: none;
            cursor: pointer;
            border: 1px solid rgba(150, 150, 150, .1);
            border-radius: 15px;
            display: inline-block;
            padding: 10px 15px;
            margin: 0 0 15px 0;
            color: #fff;
            transition: all .2s ease;
        }
        
        .inline:hover {
            border: 1px solid rgba(120, 120, 120, .1);
            background: rgba(0, 0, 0, .1);
        }
        
        .commands {
            font-size: 14px;
            color: #ddd;
        }
        
        hr {
            width: 80%;
            outline: none;
            border: none;
            height: 1px;
            background: #444;
        }
    </style>
</head>

<body>
    <input type="text" class="search" onkeyup="search()">
    <div class="mods">
        <span>
</span>
        <div class="mod_window">
            <div class="mod_description"></div>
            <div class="inline inline_install">💓 Install</div>
            <div class="inline inline_open">✨ Show code</div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script type="text/javascript">
        const delay = .05;
        var mods = [{
            "chars": 16081,
            "commands": [".gug", ".gh", ".yt ", ".ph", ".pda "],
            "cws": 16053,
            "desc": "Create special links",
            "file": "createlinks.py",
            "lines": 435,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/createlinks.py",
            "name": "CreateLinks",
            "pic": "https://te.legra.ph/file/388e1b26a46a8c439e479.png",
            "sha": "a30a8c49479479cdee626248f7bd362dad9c4391"
        }, {
            "chars": 5631,
            "commands": [".cutelist"],
            "cws": 5603,
            "desc": "Selected voices from @hikka_neko",
            "file": "meowvoices.py",
            "lines": 169,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/meowvoices.py",
            "name": "MeowVoices",
            "pic": "https://te.legra.ph/file/440d432d2977354e9b13a.png",
            "sha": "b91a5ff0c37c8599c247b7a81487ed061ba8b003"
        }, {
            "chars": 11030,
            "commands": [".ainfo"],
            "cws": 11002,
            "desc": "Show userbot info",
            "file": "amoreinfo.py",
            "lines": 232,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/amoreinfo.py",
            "name": "AmoreInfo",
            "pic": "https://te.legra.ph/file/a15f7a16c8806a5d9af1d.png",
            "sha": "42d4bb0c7415ec49f86876e00648d6cd1ce3f8bb"
        }, {
            "chars": 3768,
            "commands": [".konsp"],
            "cws": 3740,
            "desc": "Simple module to create animated stickers via bot",
            "file": "abstract.py",
            "lines": 114,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/abstract.py",
            "name": "Abstract",
            "pic": "https://te.legra.ph/file/868a280910e7f61f6ab0e.png",
            "sha": "f1f72dc5c4c56ef4a4992967a3092e1d890ba07c"
        }, {
            "chars": 7652,
            "commands": [".instas"],
            "cws": 7624,
            "desc": "Download instagram photo/video/reels without watermark",
            "file": "instsave.py",
            "lines": 213,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/instsave.py",
            "name": "InstSave",
            "pic": "https://te.legra.ph/file/0251f5d602a8f32cd7368.png",
            "sha": "02e31c77216578bab74e3cac0ce485b268d0fb47"
        }, {
            "chars": 7327,
            "commands": [".thup"],
            "cws": 7297,
            "desc": "Upload video or photo to telegraph",
            "file": "telegraphup.py",
            "lines": 244,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/telegraphup.py",
            "name": "Telegraphup",
            "pic": "https://te.legra.ph/file/5ef64ee0466032d8a4687.png",
            "sha": "e3c51c65d8db0c627ddc5c08767c7dd41af57e47"
        }, {
            "chars": 8228,
            "commands": [".bull", ".bulli"],
            "cws": 8200,
            "desc": "Can severely offend the interlocutor with obscenities",
            "file": "bull.py",
            "lines": 252,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/bull.py",
            "name": "Bull",
            "pic": "https://te.legra.ph/file/7772a7dae6290f0a612a6.png",
            "sha": "89df8e3e6b7d533652fa79ea11cea9d7df795e66"
        }, {
            "chars": 12552,
            "commands": [".help animevoices"],
            "cws": 12518,
            "desc": "Various anime voices",
            "file": "animevoices.py",
            "lines": 321,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/animevoices.py",
            "name": "AnimeVoices",
            "pic": "https://cdn-icons-png.flaticon.com/128/1599/1599516.png",
            "sha": "2895cfd72185683510f05cafad9860a4af77586e"
        }, {
            "chars": 27589,
            "commands": [".imgbb"],
            "cws": 27543,
            "desc": "Upload your photo/video/gif to https://ibb.co",
            "file": "imgbb.py",
            "lines": 703,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/imgbb.py",
            "name": "BanStickers",
            "pic": "https://cdn-icons-png.flaticon.com/128/892/892311.png",
            "sha": "eed3f6906a4b9498d4afcec63d1ef97447cabf63"
        }, {
            "chars": 16622,
            "commands": [".mydiary"],
            "cws": 16592,
            "desc": "Here you can write your diary or notes",
            "file": "mydiary.py",
            "lines": 487,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/mydiary.py",
            "name": "MyDiary",
            "pic": "https://cdn-icons-png.flaticon.com/512/3238/3238016.png",
            "sha": "2c848beea12d1bc4f4f0651358947ad3efbe30e2"
        }, {
            "chars": 2671,
            "commands": [".hacker"],
            "cws": 2589,
            "desc": "Makes sticker text with hacker",
            "file": "hacker.py",
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/hacker.py",
            "name": "Hacker",
            "pic": "https://cdn-icons-png.flaticon.com/128/924/924915.png",
            "sha": "7d287ba9dce4057674381529d6ad146534fb3ec4"
        }, {
            "chars": 3850,
            "commands": [".help autoprofile"],
            "cws": 3822,
            "desc": "You can set time on bio and name. And via config you may set to your timezone",
            "file": "autoprofile.py",
            "lines": 118,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/autoprofile.py",
            "name": "AutoProfile",
            "pic": "https://cdn-icons-png.flaticon.com/128/3561/3561157.png",
            "sha": "3a7ef87704a70b294a6a6f05736eb54058ef31a5"
        }, {
            "chars": 6266,
            "commands": [".frog , .twix, .glax"],
            "cws": 6236,
            "desc": "Creates amazing quotes ",
            "file": "funquotes.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/funquotes.py",
            "name": "FunQuotes",
            "pic": "https://cdn-icons-png.flaticon.com/128/2190/2190622.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }, {
            "chars": 6266,
            "commands": [".pinfo"],
            "cws": 6236,
            "desc": "Premium emoji, no inline",
            "file": "premiuminfo.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/premiuminfo.py",
            "name": "PremiumInfo",
            "pic": "https://cdn-icons-png.flaticon.com/128/1458/1458256.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }, {
            "chars": 6266,
            "commands": [".trig"],
            "cws": 6236,
            "desc": "Make trigger gif",
            "file": "tigger.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/trigger.py",
            "name": "Trigger",
            "pic": "https://cdn-icons-png.flaticon.com/128/3590/3590408.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }, {
            "chars": 6266,
            "commands": [".afacts"],
            "cws": 6236,
            "desc": "Interesting facts",
            "file": "facts.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/facts.py",
            "name": "Facts",
            "pic": "https://cdn-icons-png.flaticon.com/128/5558/5558278.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }, {
            "chars": 6266,
            "commands": [".capt"],
            "cws": 6236,
            "desc": "Make cartoon photo",
            "file": "cartoonimg.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/cartoonimfg.py",
            "name": "CartoonIMG",
            "pic": "https://cdn-icons-png.flaticon.com/128/2541/2541502.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }, {
            "chars": 6266,
            "commands": [".atime, .atimei"],
            "cws": 6236,
            "desc": "See the time of other countries",
            "file": "univtime.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/univtime.py",
            "name": "UniversalTime",
            "pic": "https://cdn-icons-png.flaticon.com/128/2340/2340162.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }, {
            "chars": 6266,
            "commands": [".iping"],
            "cws": 6236,
            "desc": "Just ping which work on inline",
            "file": "ilineping.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/inlineping.py",
            "name": "InlinePing",
            "pic": "https://cdn-icons-png.flaticon.com/512/7400/7400864.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }, {
            "chars": 6266,
            "commands": [".cfgdtwr"],
            "cws": 6236,
            "desc": "Don't tag without reason, before using set config",
            "file": "dtwr.py",
            "lines": 177,
            "link": "https://raw.githubusercontent.com/AmoreForever/amoremods/master/dtwr.py",
            "name": "DTWR",
            "pic": "https://cdn-icons-png.flaticon.com/128/2752/2752990.png",
            "sha": "3e4eea86370eff34b89fa01cb74c245519a19a17"
        }];
        for (var i = 0; i < mods.length; i++) {
            var mod = mods[i];
            let file = mod['link'].split('/');
            file = file[file.length - 1];
            let random = (Math.random() * (-.4) + .7).toFixed(3);
            document.querySelector('.mods span').innerHTML += '<div class="mod" id="m' + i.toString() + '" name="' + mod['name'] + '"><div class="flex"><img class="icon" src="' + mod['pic'] + '"<a class="title" href="view/' + file + '" target="_blank">' + mod['name'] + '</a></div></div>';
            $("#m" + i.toString()).hide();
        }
        setTimeout(() => {
            for (var i = 0; i < mods.length; i++) {
                $("#m" + i.toString()).fadeIn(500);
            }
        }, 1000);

        $(".mod_window").hide();

        const h = window.innerHeight;

        var mod_e = document.querySelectorAll('.mod');
        for (var i = 0; i < mod_e.length; i++) {
            var mod = mod_e[i];
            mod.onmouseover = (e) => {
                $(".mod_window").fadeIn(50);
                $(".mod_description").attr('id', e.currentTarget.id);
                let desc = mods[parseInt($(".mod_description").attr('id').substr(1))];
                let cmds = "";
                if (desc['commands'].length > 0) {
                    cmds = '<br><hr>' + '<span class="commands">' + desc['commands'].join(' ') + '</span>';
                }
                $(".mod_description").html(desc['desc'] + cmds);

                let left = e.currentTarget.offsetLeft;
                if (left + document.querySelector('.mod_window').offsetWidth > window.innerWidth) {
                    left = window.innerWidth - document.querySelector('.mod_window').offsetWidth - 10;
                }
                let top = e.currentTarget.offsetTop + e.currentTarget.offsetHeight + 5;
                if (top + document.querySelector('.mod_window').offsetHeight > h) {
                    left += e.currentTarget.offsetWidth + 10;
                    top = h - document.querySelector('.mod_window').offsetHeight - 10;
                }
                $(".mod_window").css({
                    "margin-left": left.toString() + "px",
                    "margin-top": top.toString() + "px"
                });
            }

            mod.onmouseout = (e) => {
                setTimeout(() => {
                    if ($(".mod_window").is(':hover') || document.querySelector('.mod:hover')) {
                        return
                    }
                    $(".mod_window").fadeOut(50);
                }, 150);
            }
        }
        document.querySelector('.mod_window').onmouseout = (e) => {
            setTimeout(() => {
                if ($(".mod_window").is(':hover') || document.querySelector('.mod:hover')) {
                    return
                }
                $(".mod_window").fadeOut(50);
            }, 150);
        }
        const hearts = ['❤️', '🧡', '💛', '💙', '💚', '💜', '🖤', '🤍'];
        document.querySelector('.inline_install').onclick = (e) => {
            navigator.clipboard.writeText(".dlmod https://github.com/AmoreForever/amoremods/raw/master/" + mods[parseInt($(".mod_description").attr('id').substr(1))]['file']);
            e.currentTarget.innerHTML = hearts[Math.floor(Math.random() * hearts.length)] + ' Copied';
            setTimeout(() => {
                $(".inline_install").html("📥 Install");
            }, 1000);
        }

        document.querySelector('.inline_open').onclick = (e) => {
            window.open("https://github.com/AmoreForever/amoremods/raw/master/" + mods[parseInt($(".mod_description").attr('id').substr(1))]['file'], target = "_blank");
        }
        setInterval(function() {
            document.querySelector('input').focus();
        }, 500);

        function search() {
            let query = document.querySelector('input').value;
            let mods = document.querySelectorAll('.mod');
            for (var i = 0; i < mods.length; i++) {
                let mod = mods[i];
                mod.classList.remove('selected');
                if (!mod.getAttribute('name').toLowerCase().includes(query.toLowerCase())) {
                    mod.classList.add('hidden');
                } else {
                    mod.classList.remove('hidden');
                    if (query !== "") {
                        mod.classList.add('selected');
                    }
                }
            }

        }
    </script>
</body>

</html
