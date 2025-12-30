import os
from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.getcwd(), filename)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Birthday Gift For You</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Caveat:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            margin:0; font-family:'Poppins', sans-serif;
            background: linear-gradient(135deg,#ffd3e9,#cfe7ff);
            min-height:100vh; display:flex; justify-content:center; align-items:center;
            overflow-x:hidden; position:relative;
        }
        
        /* Floating Sticker */
        .emblem-wrapper {
            position:fixed; top:15px; right:15px; width:70px; height:70px; 
            animation: emblemFloat 3s ease-in-out infinite; z-index: 100;
        }
        @keyframes emblemFloat {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-10px) rotate(8deg); }
        }
        .emblem { width:100%; filter: drop-shadow(0 0 5px rgba(0,0,0,0.1)); }

        /* Pages System */
        .page { 
            position:absolute; width:90%; max-width:450px; text-align:center; 
            transition: all 0.6s ease; opacity:0; pointer-events:none;
        }
        .show { opacity:1 !important; pointer-events:auto !important; transform:translateY(0) !important; position: relative; }

        .btn {
            padding:12px 25px; background:#ff82a9; color:white; border:none; 
            border-radius:50px; font-size:16px; font-weight:600; cursor:pointer; 
            transition:.3s; box-shadow: 0 4px 15px rgba(255,130,169,0.4); margin-top: 15px;
        }
        .btn:hover { transform:scale(1.05); background:#ff6c99; }
        
        .card { 
            background:#fff; border-radius:20px; padding:25px; 
            box-shadow:0 15px 35px rgba(0,0,0,0.1); margin-bottom: 20px;
        }

        /* Kado Animation */
        #giftEmoji { font-size:90px; cursor:pointer; margin-bottom: 20px; animation: giftBounce 1.2s ease-in-out infinite; }
        @keyframes giftBounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }

        /* Gallery Landscape */
        #pageGallery { display: none; width: 100%; max-width: 600px; padding: 20px; box-sizing: border-box; }
        .gallery-list { display: flex; flex-direction: column; gap: 25px; width: 100%; }
        .photo-item { 
            background: white; padding: 12px; border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.08); transform: rotate(-1deg);
        }
        .photo-item:nth-child(even) { transform: rotate(1deg); }
        .photo-item img { 
            width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 5px;
        }
        .photo-item p { font-family: 'Caveat', cursive; font-size: 20px; margin: 10px 0 0 0; color: #444; }

        /* Textarea for Message */
        textarea {
            width: 100%; height: 120px; padding: 15px; border-radius: 15px;
            border: 2px solid #ffd3e9; font-family: inherit; font-size: 15px;
            box-sizing: border-box; outline: none; margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="emblem-wrapper">
    <img class="emblem" src="https://cdn-icons-png.flaticon.com/512/1147/1147981.png">
</div>

<audio id="birthdaySong" src="https://files.catbox.moe/wsgxyt.mp4" loop></audio>

<div id="page1" class="page show">
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
        <button class="btn" onclick="showGallery()">Lihat Kenangan ✨</button>
    </div>
</div>

<div id="pageGallery">
    <h2 style="color:#ff6c99; font-family:'Caveat', cursive; font-size:35px; text-align:center;">Our Memories ❤️</h2>
    <div class="gallery-list">
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=1"><p>Ingat momen ini? Lucu banget!</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=2"><p>Pas kita lagi jalan bareng 🌸</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=3"><p>Senyum kamu favorit aku ✨</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=4"><p>Definisi bahagia itu sederhana.</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=5"><p>Terima kasih sudah bertahan ya.</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=6"><p>Semoga kita begini terus.</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=7"><p>Kamu yang terbaik!</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=8"><p>Sehat selalu ya kamu.</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=9"><p>Satu kata: Keren!</p></div>
        <div class="photo-item"><img src="https://picsum.photos/600/350?random=10"><p>I Love You! ❤️</p></div>
    </div>
    <div style="text-align: center; margin: 30px 0;">
        <button class="btn" onclick="showFinalMessage()">Tulis Pesan untukku ✨</button>
    </div>
</div>

<div id="pageFinal" class="page">
    <div class="card">
        <h2>Kirim Pesan 🎉</h2>
        <p>Tulis harapan atau pesanmu di sini yaa:</p>
        <textarea id="pesanWA" placeholder="Tulis sesuatu yang manis..."></textarea>
        <button class="btn" style="background: #25d366;" onclick="kirimKeWA()">Kirim ke WhatsApp 📱</button>
    </div>
</div>

<script>
let userNama = "";
let userUmur = "";
// GANTI NOMOR WA DI SINI (Gunakan format 628xxx)
const nomorWA = "6281234567890"; 

function switchPage(id){
    document.querySelectorAll('.page').forEach(p => p.classList.remove('show'));
    setTimeout(() => { 
        const target = document.getElementById(id);
        if(target) target.classList.add('show');
    }, 300);
}

function startSurprise(){
    userNama = document.getElementById('nama').value || "Sayang";
    userUmur = document.getElementById('umur').value || "Spesial";
    switchPage('page3');
    let time = 3;
    const tDisplay = document.getElementById('timer');
    const countdown = setInterval(() => {
        time--;
        tDisplay.textContent = time;
        if(time <= 0){
            clearInterval(countdown);
            switchPage('page4');
        }
    }, 1000);
}

function revealCard(){
    document.getElementById('birthdaySong').play();
    const ucapan = document.getElementById('ucapanText');
    ucapan.innerHTML = `Happy Birthday, <br><span style="color:#ff82a9; font-size:35px;">${userNama}!</span> 🎉<br><br>Gak terasa sekarang udah ${userUmur} tahun. Stay amazing!`;
    switchPage('page5');
}

function showGallery(){
    document.querySelectorAll('.page').forEach(p => p.style.display = 'none');
    document.getElementById('pageGallery').style.display = 'block';
    document.body.style.overflowY = 'auto';
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function showFinalMessage(){
    document.getElementById('pageGallery').style.display = 'none';
    const final = document.getElementById('pageFinal');
    final.style.display = 'block';
    setTimeout(() => final.classList.add('show'), 100);
    window.scrollTo({top: 0, behavior: 'smooth'});
    document.body.style.overflowY = 'hidden';
}

function kirimKeWA(){
    const pesan = document.getElementById('pesanWA').value;
    if(!pesan){
        alert("Tulis pesannya dulu dong 🤭");
        return;
    }
    const teksWA = `Halo! Aku ${userNama} (${userUmur}th). %0A%0AIni pesan dariku: %0A"${pesan}"`;
    window.open(`https://wa.me/${nomorWA}?text=${teksWA}`, '_blank');
}
</script>
</body>
</html>
""")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
