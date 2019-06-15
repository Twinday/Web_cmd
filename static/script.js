function add_message() {
            $.ajax({
                type: "POST",
                url: "/add_message",
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    var json = jQuery.parseJSON(response)
                    var ddd = $("div[role=result]")
                    var cmd1 = $("<div/>").addClass("message").appendTo(ddd);
                    $("<pre/>").appendTo($("<h2/>").appendTo(cmd1)).html(json.com);
                    var cmd2 = $("<div/>").addClass("message").appendTo(ddd);
                    $("<pre/>").appendTo($("<h2/>").appendTo(cmd2)).html(json.mess);
                    //$("<pre/>").appendTo($("<h2/>").appendTo(cmd)).html(json.mess);
                    //$('#divcommand').html(json.com)
                    //$('#divmessage').html(json.mess)
                    document.getElementById("input").value = "";
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
