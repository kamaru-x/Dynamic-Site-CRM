$(document).ready(function(){
    // $('input[name="title"]').on('keyup', function(){
    //     var value = $("input[name='title']").val();
    //     $('input[name="url"]').val(value);
    //     });

    // $('#offer_price').on('blur',function(){
    //     var actual_price = $('#actual_price').val();
    //     var offer_price = $('#offer_price').val();
    //     if(actual_price < offer_price){
    //         alert(offer_price)
    //     }else{
    //         pass
    //     }
    // });

    $('#offer_price').blur(function(){
        actual_price = $('#actual_price').val()
        offer_price = $('#offer_price').val()
        
        if(parseInt(actual_price) < parseInt(offer_price)){
            alert('offer price must be less than actual price')
        }
    })
})