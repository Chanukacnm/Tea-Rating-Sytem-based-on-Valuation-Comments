$(document).ready(function(){
  $("#target").on('submit',function(){
      // alert("It works");
     
  });

  // $("#tbb").toggleClass("blur");
  //   setTimeout(function(){ $("#tbb").toggleClass("blur"); }, 400);

  var tbb = document.getElementById('tbb');
  var tbl = document.getElementById('tbl');
  var tblLen = tbb.rows.length;
  if(tblLen>1){
    tbb.style.border="1px solid #000000";
    tbl.style.backgroundColor = "rgb(224, 224, 224)";
    tbl.style.padding = "4px";
  }
  // console.log("len=>", tblLen);
  for(var i=1; i<tblLen; i++){
    var tblPred = tbb.rows[i].cells[3].innerHTML;
    if(tblPred == 1){
      // console.log("Pre1=>", tblPred);
      
      tbb.rows[i].cells[2].style.color  = "green";
    }
    if(tblPred == 0){
      // console.log("Pre0=>", tblPred);
      tbb.rows[i].cells[2].style.color  = "red";
    }
  }
  $('td:nth-child(4),th:nth-child(4)').hide();
});

// $(function(){
//   $('#predictResult').change(function(){
//     var tbb = document.getElementById('tbb');
//     var tblLen = tbb.rows.length;
//     console.log("len=>", tblLen);
//     for(var i=1; i<tblLen; i++){
//       var tblPred = tbb.rows[i].cells[3].innerHTML;
//       if(tblPred == 1){
//         // console.log("Pre1=>", tblPred);
        
//         tbb.rows[i].cells[2].style.color  = "green";
//       }
//       if(tblPred == 0){
//         // console.log("Pre0=>", tblPred);
//         tbb.rows[i].cells[2].style.color  = "red";
//       }
//     }
//     $('td:nth-child(4),th:nth-child(4)').hide();
    
//   });
// });



// $(document).ready(function() {   //same as: $(function() { 
//   alert("hi 1");
// });

// $(window).load(function() {
//   alert("hi 2");
// });

// $(document).ready(function(){
//   $("input").change(function(){
    
//     var tbb = document.getElementById('tbb');
//     var tblLen = tbb.rows.length;
//     console.log("len=>", tblLen);
//     for(var i=1; i<tblLen; i++){
//       var tblPred = tbb.rows[i].cells[3].innerHTML;
//       if(tblPred == 1){
//         console.log("Pre1=>", tblPred);
        
//         tbb.rows[i].cells[3].style.backgroundColor = "green";
//       }
//       if(tblPred == 0){
//         console.log("Pre0=>", tblPred);
//         tbb.rows[i].cells[3].style.backgroundColor = "red";
//       }
      
//       // var customerId = $(this).find("td:last-child").html(); 
//       // console.log("Pre=>",customerId)
//     }
//   //   $('#tbb tbody tr').each(function() {
//   //     // for(var i=1; i<2; i++){
//   //     //   console.log("vvv=>", tbb.rows[i].cells[3].innerHTML);
//   //     //   // var customerId = $(this).find("td:last-child").html(); 
//   //     //   // console.log("Pre=>",customerId)
//   //     // }

      
      
//   //  });
    
//   //   // for (var i = 0, row; row = table.rows[i]; i++) {
//   //   //   for (var j = 0, col; col = row.cells[j]; j++) {
        
//   //   //       var sss = $(this).find('td').text();
//   //   //       console.log("sss=>", sss);
      
//   //   //   } 
//   //   // }
//   //   $("#tbb tbody tr").each(function() {

//   //     // Within tr we find the last td child element and get content
//   //     // console.log("cc");
//   //     // console.log("Last",$(this).find("td:last-child").html());
//   //     // var predicion = $(this).closest('tr').find('#Pred').text();
//   //     // var Comments1 = $(this).closest('tr').find('#Com1').text();
//   //     // console.log("predicion=>",predicion);
//   //     // console.log("Comments=>",Comments1);
     

//   //   });


//   });
// });
// $(document).ready(function(){
//    $("input").change(function(){
//     setTimeout(function(){

//       predictResult()
//     }, 5000)
//   })
// });
