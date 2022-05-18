  function ref(){
     
      var z = document.getElementById('qr').style.opacity
      // alert(z)
      if (z > 0.5) {
         // alert("Помни! \n Это твой шанс!")
        document.getElementById('qr').style.opacity = "0.05"
      }
      else {
        document.getElementById('qr').style.opacity = "1"
      }
    }