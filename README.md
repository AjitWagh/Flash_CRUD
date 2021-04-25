# Flash_CRUD
Flask Dashboard



https://teams.microsoft.com/l/meetup-join/19%3ameeting_NjJhNWFlYWMtYmJlZS00YjkyLThkOTMtYTFjZTcwYmUzZGYx%40thread.v2/0?context=%7b%22Tid%22%3a%22ac0208f1-f65d-4e1e-be1d-e62cf55ca6ff%22%2c%22Oid%22%3a%22769b4a6b-bcc9-429e-82b2-d3938046b216%22%7d





<!-- Script -->


<script>
$(document).ready(function(){
    $.datepicker.setDefaults({
        dateFormat: 'yy-mm-dd'
    });
    $(function(){
        $("#From").datepicker();
        $("#to").datepicker();
    });
    $('#range').click(function(){
        var From = $('#From').val();
        var to = $('#to').val();
        if(From != '' && to != '')
        {
            $.ajax({
                url:"/range",
                method:"POST",
                data:{From:From, to:to},
                success:function(data)
                {
                    $('#purchase_order').html(data);
                    $('#purchase_order').append(data.htmlresponse);
                }
            });
        }
        else
        {
            alert("Please Select the Date");
        }
    });
});
</script>
