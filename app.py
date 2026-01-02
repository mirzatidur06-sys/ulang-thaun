<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Birthday Gift For You</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Caveat:wght@700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --pink-primary: #ff82a9;
            --pink-hover: #ff6c99;
            --bg-gradient: linear-gradient(135deg,#ffd3e9,#cfe7ff);
        }

        body {
            margin:0; font-family:'Poppins', sans-serif;
            background: var(--bg-gradient);
            min-height:100vh; display:flex; justify-content:center; align-items:center;
            overflow-x:hidden; position:relative;
        }

        .fairy-lights {
            position: fixed; top: 0; left: 0; width: 100%; height: 60px;
            background-image: url('https://files.catbox.moe/pvhf2s.png');
            background-repeat: repeat-x; background-size: contain;
            z-index: 1000; pointer-events: none;
        }

        @keyframes slideUpFade {
            from { opacity: 0; transform: translateY(30px) scale(0.95); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        .page { 
            position:absolute; width:90%; max-width:450px; text-align:center; 
            display: none; opacity: 0; z-index: 10;
        }

        .page.show { 
            display: block;
            animation: slideUpFade 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
        }

        #fallingEnvelope {
            position: fixed; top: -100px; left: 50%; transform: translateX(-50%);
            font-size: 50px; cursor: pointer; z-index: 100;
            display: none; transition: top 3s ease-in-out;
        }
        @keyframes sway {
            0%, 100% { transform: translateX(-50%) rotate(-10deg); }
            50% { transform: translateX(-50%) rotate(10deg); }
        }

        /* --- MODAL SURAT ANIMATED --- */
        .modal {
            display: none; position: fixed; z-index: 2000;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.6); justify-content: center; align-items: center;
            backdrop-filter: blur(5px);
            opacity: 0; transition: opacity 0.4s ease;
        }
        .modal.open { opacity: 1; }

        .modal-content {
            background: #fff9f0; padding: 30px; width: 85%; max-width: 400px;
            border-radius: 15px; position: relative; border: 2px solid #ff82a9;
            box-shadow: 0 10px 40px rgba(0,0,0,0.4);
            transform: scale(0.7); transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .modal.open .modal-content { transform: scale(1); }

        #isiSurat {
            font-family: 'Caveat', cursive;
            font-size: 24px; line-height: 1.4; text-align: left;
            min-height: 180px; color: #444;
            transition: all 0.4s ease;
        }

        .fade-out { opacity: 0; transform: translateX(-15px); }
        .fade-in { opacity: 1; transform: translateX(0); }
        /* --- END MODAL SURAT --- */

        .heart {
            position: fixed; color: #ff82a9; font-size: 20px;
            pointer-events: none; z-index: 999;
            animation: moveUp 4s linear forwards;
        }
        @keyframes moveUp {
            0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }

        .btn {
            padding:12px 25px; background: var(--pink-primary); color:white; border:none; 
            border-radius:50px; font-size:14px; font-weight:600; cursor:pointer; 
            transition:.3s; box-shadow: 0 4px 15px rgba(255,130,169,0.4); margin-top: 15px;
        }
        .btn:hover { transform:scale(1.05); background: var(--pink-hover); }

        .card { 
            background:#fff; border-radius:20px; padding:25px; 
            box-shadow:0 15px 35px rgba(0,0,0,0.1); margin-bottom: 20px;
        }

        .timer-wrapper { margin-top: 20px; display: flex; justify-content: center; gap: 10px; }
        .time-unit { background: white; padding: 10px; border-radius: 10px; min-width: 55px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
        .time-unit span { display: block; font-weight: bold; color: var(--pink-primary); font-size: 20px; }
        .time-unit label { font-size: 9px; text-transform: uppercase; color: #888; }

        #giftEmoji { font-size:90px; cursor:pointer; margin-bottom: 20px; animation: giftBounce 1.2s ease-in-out infinite; }
        @keyframes giftBounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }

        #pageGallery { display: none; width: 100%; max-width: 500px; padding: 80px 20px 40px 20px; box-sizing: border-box; }
        .gallery-list { display: flex; flex-direction: column; gap: 40px; width: 100%; }

        .photo-item { 
            background: white; padding: 12px; border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1); 
            opacity: 0; transform: translateY(60px) scale(0.9);
            transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        .photo-item.visible { opacity: 1; transform: translateY(0) scale(1) rotate(-1.5deg); }
        .photo-item:nth-child(even).visible { opacity: 1; transform: translateY(0) scale(1) rotate(1.5deg); }

        .photo-item img { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 5px; }
        .photo-item p { font-family: 'Caveat', cursive; font-size: 22px; margin: 15px 0 5px 0; color: #444; }

        #ucapanText { min-height: 100px; line-height: 1.6; white-space: pre-wrap; font-size: 18px; }

        textarea {
            width: 100%; height: 120px; padding: 15px; border-radius: 15px;
            border: 2px solid #ffd3e9; font-family: inherit; font-size: 15px;
            box-sizing: border-box; outline: none; margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="fairy-lights"></div>
<audio id="birthdaySong" src="https://files.catbox.moe/wsgxyt.mp4" loop></audio>

<div id="fallingEnvelope" onclick="openModal()">✉️</div>

<div id="suratModal" class="modal">
    <div class="modal-content">
        <div style="display:flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <h3 style="margin:0; color:var(--pink-primary); font-family: 'Poppins', sans-serif; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">A Special Letter</h3>
            <span id="pageNumber" style="font-family: 'Poppins', sans-serif; font-size: 12px; color: #888;"></span>
        </div>

        <div id="isiSurat" class="fade-in"></div>

        <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px; margin-top: 20px;">
            <button id="btnPrevSurat" class="btn" style="padding: 8px 15px; font-size: 12px; background: #bbb;" onclick="changeSuratPage(-1)">Back</button>
            <button id="btnNextSurat" class="btn" style="padding: 8px 15px; font-size: 12px;" onclick="changeSuratPage(1)">Next</button>
            <button id="btnCloseModal" class="btn" style="padding: 8px 15px; font-size: 12px; display:none;" onclick="closeModal()">Selesai ✨</button>
        </div>
    </div>
</div>

<div id="pageLocked" class="page show">
    <img style="width:120px;" src="https://cdn-icons-png.flaticon.com/512/3850/3850285.png">
    <h1 style="font-family:'Caveat', cursive; font-size: 35px;">Tunggu ya... ❤️</h1>
    <div class="timer-wrapper">
        <div class="time-unit"><span id="d">00</span><label>Hari</label></div>
        <div class="time-unit"><span id="h">00</span><label>Jam</label></div>
        <div class="time-unit"><span id="m">00</span><label>Menit</label></div>
        <div class="time-unit"><span id="s">00</span><label>Detik</label></div>
    </div>
</div>

<div id="page1" class="page">
    <img style="width:120px;" src="https://cdn-icons-png.flaticon.com/512/4392/4392525.png">
    <h1>Haii! Sebelum lanjut,<br>isi dulu data diri kamu yaa 🌸</h1>
    <button class="btn" onclick="switchPage('page2')">Gaskeun! 🚀</button>
</div>

<div id="page2" class="page">
    <div class="card">
        <h1>Kenalan dulu yuk 🤭</h1>
        <input type="text" id="nama" style="width:100%; padding:12px; margin:10px 0; border-radius:10px; border:1px solid #ddd;" placeholder="Nama kamu">
        <input type="number" id="umur" style="width:100%; padding:12px; margin:10px 0; border-radius:10px; border:1px solid #ddd;" placeholder="Umur kamu?">
        <button class="btn" onclick="startSurprise()">Kirim & Lihat Kejutan ~</button>
    </div>
</div>

<div id="page3" class="page">
    <h1>Menyiapkan Kejutan...</h1>
    <div id="timer" style="font-size:60px; font-weight:bold; color:#ff82a9;">3</div>
</div>

<div id="page4" class="page">
    <div id="giftEmoji" onclick="revealCard()">🎁</div>
    <h2>Klik kadonya! ✨</h2>
</div>

<div id="page5" class="page">
    <div class="card">
        <h2 id="ucapanText"></h2>
        <p id="instruction" style="display:none; color:#888; font-size:12px;">Eh, ada surat jatuh? Coba di-klik! ✉️</p>
        <button id="btnGallery" class="btn" style="display:none;" onclick="showGallery()">Lihat Kenangan ✨</button>
    </div>
</div>

<div id="pageGallery">
    <h2 style="color:#ff6c99; font-family:'Caveat', cursive; font-size:40px; text-align:center; margin-bottom: 40px;">Our Memories ❤️</h2>
    <div class="gallery-list">
        <div class="photo-item"><img src="https://files.catbox.moe/wfyphd.png"><p>Foto berdua kita yang menurutku paling romantis+lucu</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/na59r1.png"><p>Ni aku gendong orang terlucu di dunia</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/ezpsil.png"><p>Pas kita main konon ni yang kamu bilang berani</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/2o84c5.png"><p>Pas naik gunung ni awal awal hts</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/m4gjt7.png"><p>Makasih yahh dah mau nolongin</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/62rvez.png"><p>Semoga kita begini terus yahh</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/s04vxf.png"><p>Nanti jatuh nangis eluu</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/kuv421.png"><p>Sehat selalu ya kamu.</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/g23me7.png"><p>Satu kata: imutt!</p></div>
        <div class="photo-item"><img src="https://files.catbox.moe/slczyl.png"><p>Pertama x kita foto ni sama teman kita</p></div>
    </div>
    <div style="text-align: center; margin: 50px 0;">
        <button class="btn" onclick="showFinalMessage()">Tulis Pesan untukku ✨</button>
    </div>
</div>

<div id="pageFinal" class="page">
    <div class="card">
        <h2>Kirim Pesan 🎉</h2>
        <p>Tulis harapan atau pesanmu di sini yaa:</p>
        <textarea id="pesanWA" placeholder="Tulis sesuatu yang manis..."></textarea>
        <button class="btn" onclick="goToThanksPage()">Selanjutnya ✨</button>
    </div>
</div>

<div id="pageThanks" class="page">
    <div class="card">
        <img style="width:100px; margin-bottom: 10px;" src="https://cdn-icons-png.flaticon.com/512/8204/8204222.png">
        <h2 style="font-family:'Caveat', cursive; font-size: 30px;">Makasih sudah ngisi yah! ❤️</h2>
        <p>Klik tombol di bawah untuk kirim pesannya ke WhatsApp aku yaa.</p>
        <button class="btn" style="background: #25d366;" onclick="kirimKeWA()">Kirim ke WhatsApp 📱</button>
    </div>
</div>

<script>
const targetDate = new Date("Dec 31, 2025 20:00:00").getTime();
let userNama = "";
let userUmur = "";
const nomorWA = "6281264247474"; 
let heartInterval;
let currentSuratPage = 0;
let isiHalamanSurat = [];

const intervalTimer = setInterval(function() {
    const now = new Date().getTime();
    const distance = targetDate - now;
    document.getElementById("d").innerHTML = Math.max(0, Math.floor(distance / (1000 * 60 * 60 * 24)));
    document.getElementById("h").innerHTML = Math.max(0, Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)));
    document.getElementById("m").innerHTML = Math.max(0, Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)));
    document.getElementById("s").innerHTML = Math.max(0, Math.floor((distance % (1000 * 60)) / 1000));
    if (distance <= 0) {
        clearInterval(intervalTimer);
        if(document.getElementById('pageLocked').classList.contains('show')) switchPage('page1');
    }
}, 1000);

function switchPage(id){
    const current = document.querySelector('.page.show');
    const next = document.getElementById(id);
    if(current){
        current.style.opacity = '0';
        setTimeout(() => {
            current.classList.remove('show');
            current.style.display = 'none';
            next.style.display = 'block';
            setTimeout(() => next.classList.add('show'), 50);
        }, 400);
    } else {
        next.style.display = 'block';
        next.classList.add('show');
    }
}

function startSurprise(){
    userNama = document.getElementById('nama').value || "Sayang";
    userUmur = document.getElementById('umur').value || "Spesial";
    switchPage('page3');
    let time = 3;
    const countdown = setInterval(() => {
        time--;
        document.getElementById('timer').textContent = time;
        if(time <= 0){ clearInterval(countdown); switchPage('page4'); }
    }, 1000);
}

function revealCard(){
    document.getElementById('birthdaySong').play();
    confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
    switchPage('page5');
    const text = `Happy Birthday, ${userNama}! 🎉\n\nGak terasa sekarang udah ${userUmur} tahun aja... ❤️`;
    let i = 0;
    const container = document.getElementById('ucapanText');
    function typeWriter() {
        if (i < text.length) {
            container.innerHTML += text.charAt(i).replace(/\n/g, '<br>');
            i++;
            setTimeout(typeWriter, 50);
        } else {
            dropEnvelope();
        }
    }
    setTimeout(typeWriter, 1000);
}

function dropEnvelope() {
    const env = document.getElementById('fallingEnvelope');
    env.style.display = 'block';
    setTimeout(() => {
        env.style.top = '70%'; 
        env.style.animation = 'sway 2s ease-in-out infinite';
        document.getElementById('instruction').style.display = 'block';
    }, 100);
}

// BUKA MODAL DENGAN ANIMASI
function openModal() {
    isiHalamanSurat = [
        `Hai ${userNama}, ini surat rahasia buat kamu. Aku cuma mau bilang kalau aku beruntung banget bisa kenal kamu dan ada di samping kamu sampai detik ini.`,
        `Gak kerasa ya waktu cepat banget berlalu. Banyak momen yang udah kita lewati bareng, dari yang lucu sampai yang bikin baper. Kamu selalu bisa bikin hari-hariku lebih berwarna.`,
        `Di umur yang ke-${userUmur} ini, aku berharap kamu selalu sehat, makin dewasa, dan tetap jadi orang yang ceria. Jangan pernah menyerah sama mimpi-mimpimu ya!`,
        `Semoga semua cita-citamu tercapai dan kita tetap bisa sama-sama terus. Kamu itu berharga banget buat aku. Sekali lagi, Happy Birthday! Love you! ❤️`
    ];
    currentSuratPage = 0;
    updateSuratContent();

    const modal = document.getElementById('suratModal');
    modal.style.display = 'flex';
    setTimeout(() => modal.classList.add('open'), 10); // Mulai animasi

    document.getElementById('fallingEnvelope').style.display = 'none';
    document.getElementById('instruction').style.display = 'none';
}

function updateSuratContent() {
    const isi = document.getElementById('isiSurat');
    const pNum = document.getElementById('pageNumber');
    const btnNext = document.getElementById('btnNextSurat');
    const btnPrev = document.getElementById('btnPrevSurat');
    const btnClose = document.getElementById('btnCloseModal');

    isi.classList.remove('fade-in');
    isi.classList.add('fade-out');

    setTimeout(() => {
        isi.innerHTML = isiHalamanSurat[currentSuratPage];
        pNum.innerText = `${currentSuratPage + 1} / 4`;
        isi.classList.remove('fade-out');
        isi.classList.add('fade-in');

        btnPrev.style.visibility = (currentSuratPage === 0) ? 'hidden' : 'visible';

        if (currentSuratPage === isiHalamanSurat.length - 1) {
            btnNext.style.display = 'none';
            btnClose.style.display = 'inline-block';
        } else {
            btnNext.style.display = 'inline-block';
            btnClose.style.display = 'none';
        }
    }, 300);
}

function changeSuratPage(step) {
    currentSuratPage += step;
    updateSuratContent();
}

// TUTUP MODAL DENGAN ANIMASI
function closeModal() {
    const modal = document.getElementById('suratModal');
    modal.classList.remove('open'); // Jalankan animasi tutup

    setTimeout(() => {
        modal.style.display = 'none';
        document.getElementById('btnGallery').style.display = 'inline-block';
    }, 400); // Tunggu animasi selesai (400ms)
}

function createHeart() {
    const heart = document.createElement('div');
    heart.classList.add('heart');
    heart.innerHTML = '❤️';
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.animationDuration = (Math.random() * 2 + 3) + 's';
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 4000);
}

function showGallery(){
    document.querySelectorAll('.page').forEach(p => { p.classList.remove('show'); p.style.display = 'none'; });
    const gallery = document.getElementById('pageGallery');
    gallery.style.display = 'block';
    document.body.style.overflowY = 'auto';
    heartInterval = setInterval(createHeart, 400);
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.15 });
    document.querySelectorAll('.photo-item').forEach(item => observer.observe(item));
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function showFinalMessage(){
    clearInterval(heartInterval);
    document.getElementById('pageGallery').style.display = 'none';
    document.body.style.overflowY = 'hidden';
    switchPage('pageFinal');
}

function goToThanksPage() {
    switchPage('pageThanks');
}

function kirimKeWA(){
    const pesan = document.getElementById('pesanWA').value;
    const teksWA = `Halo! Aku ${userNama}. %0A%0AIni pesan dariku: %0A"${pesan}"`;
    window.open(`https://wa.me/${nomorWA}?text=${teksWA}`, '_blank');
}
</script>
</body>
</html>
