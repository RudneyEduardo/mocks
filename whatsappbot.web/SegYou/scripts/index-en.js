var redirect_uri = "";
var refresh_token = "";
var access_token = "";
var token_type = "";
var expires_in = "";
var grant_partner = "";

var DocIdProtocol = "";
var ProposalProtocol = "";

var grantCodeSettings = {
    "url": "https://api-openbanking.sensedia.com/sandbox/auth-partner/v1/grant-code?response_type=code&client_id=fd6b02ca-2fb5-327d-8d2c-fafc7211edcd&redirect_uri=http://supermock.demo.sensedia.com&state=test123456",
    "method": "GET",
    "timeout": 0,
    "headers": {
        "callback": "0"
    },
};

$(document).ready(function(){
    document.getElementById("defaultOpen").click();
})

function setAccessTokenSettings(redirect_uri) {
    var redirect_uri_code = "";
    redirect_uri_code = redirect_uri.split('=')[2];
    redirect_uri_code = redirect_uri_code.split('&')[0];

    return {
        "url": "https://api-openbanking.sensedia.com/sandbox/auth-partner/v1/access-token",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic ZmQ2YjAyY2EtMmZiNS0zMjdkLThkMmMtZmFmYzcyMTFlZGNkOjk5NjFjNzFiLTg4OTEtM2M3My1hMTFiLTAzNjViZmFkNmY0MQ=="
        },
        "data": {
            "grant_type": "authorization_code",
            "code": redirect_uri_code
        }
    };
}

function setRefeshTokenSettings(refresh_token) {
    return {
        "url": "https://api-openbanking.sensedia.com/sandbox/auth-partner/v1/access-token",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic ZmQ2YjAyY2EtMmZiNS0zMjdkLThkMmMtZmFmYzcyMTFlZGNkOjk5NjFjNzFiLTg4OTEtM2M3My1hMTFiLTAzNjViZmFkNmY0MQ=="
        },
        "data": {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
    };
}

function setRequestDocId(access_token, DocId) {
    return {
        "url": "https://api-openbanking.sensedia.com/poc/basic-retail/Inquiries/" + DocId + "/asynchronous",
        "method": "GET",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        },
    };
}

function setPathConfirmSettings(access_token, DocId) {
    var settings = {
        "url": "https://api-openbanking.sensedia.com/poc/basic-retail/Inquiries/" + DocId + "/asynchronous/" + DocIdProtocol,
        "method": "PATCH",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,
            // "User-Agent": "PostmanRuntime/7.25.0",
            // "Host": "http://jquery.com",
            // "Origin": "http://jquery.com"
        },
    };
}

function setDeleteDocIdSettings(access_token, DocId) {
    return {
        "url": "https://api-openbanking.sensedia.com/poc/basic-retail/Inquiries/" + DocId + "/asynchronous/" + DocIdProtocol,
        "method": "DELETE",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        },
    };

}

function setCallbackSettings(access_token, DocId) {
    return {
        "url": "https://api-openbanking.sensedia.com/poc/basic-retail/Inquiries/" + DocId + "/asynchronous/" + DocIdProtocol,
        "method": "GET",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        },
    };
}

function setCreditProposalSettings(access_token, tax, amount, amountTax, comment) {
    return {
        "url": "https://api-openbanking.sensedia.com/poc/basic-retail/proposals/9394C8BD-248A-4361-B324-D55F7C2E7461/analysis",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        },
        "data": JSON.stringify(
            {
                "tax": tax,
                "amount": amount,
                "amountTax": amountTax,
                "comments": comment
            }),
    };
}

function setPatchProposalSettings(access_token, tax, amount, amountTax, comment, proposal_protocol) {
    return {
        "url": "https://api-openbanking.sensedia.com/poc/basic-retail/proposals/9394C8BD-248A-4361-B324-D55F7C2E7461/analysis/" + proposal_protocol,
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,
            // "User-Agent": "PostmanRuntime/7.25.0",
            // "Host": "http://jquery.com",
            // "Origin": "http://jquery.com"
        },
        "data": JSON.stringify({ "tax": tax, "amount": amount, "amountTax": amountTax, "comments": "" }),
    };
}

function setDeleteProposalSettings(access_token, proposal_protocol, tax, amount, amountTax, comment){
    return {
        "url": "https://api-openbanking.sensedia.com/poc/basic-retail/proposals/9394C8BD-248A-4361-B324-D55F7C2E7461/analysis/"+ proposal_protocol,
        "method": "DELETE",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/json",
          "Authorization": "Bearer "+ access_token 
        },
        "data": JSON.stringify({"tax":8,"amount":100,"amountTax":108,"comments":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin a risus vitae ex convallis ullamcorper non in felis. Suspendisse malesuada dictum nunc, ac porta sapien sagittis ut. Maecenas eu luctus ante, a varius eros."}),
      };
}

function setCallbackProposalSettings(access_token,ProposalProtocol){
return {
    "url": "https://api-openbanking.sensedia.com/poc/basic-retail/proposals/9394C8BD-248A-4361-B324-D55F7C2E7461/analysis/"+ProposalProtocol+"/status",
    "method": "GET",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + access_token
    },
    "data": JSON.stringify({"tax":8,"amount":100,"amountTax":108,"comments":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin a risus vitae ex convallis ullamcorper non in felis. Suspendisse malesuada dictum nunc, ac porta sapien sagittis ut. Maecenas eu luctus ante, a varius eros."}),
  }

}

$("#btnConnect").click(function () {
    $.ajax(setRefeshTokenSettings(refresh_token))
        .done(function (response) {
            console.log("Refresh Token Success: ");
            console.log(response);
            refresh_token = response.refresh_token;
            access_token = response.access_token;
            token_type = response.token_type;
        })
        .fail(function (response) {
            console.log("Refresh Token fail: ");
            console.log(response);
            $.ajax(grantCodeSettings).done(function (response) {
                console.log("Grant Code Success: ");
                redirect_uri = response.redirect_uri;
                console.log(response);
                $.ajax(setAccessTokenSettings(redirect_uri)).done(function (response) {
                    console.log("Access Token Success: ");
                    console.log(response);
                    refresh_token = response.refresh_token;
                    access_token = response.access_token;
                    token_type = response.token_type;

                    $("#Content").show();
                }).fail(function (response) {
                    console.log("Access Token fail: ");
                    console.log(response);
                })
            })
                .fail(function (response) {
                    console.log("Grant Code fail: ");
                    console.log(response);
                });
        });

})

$("#btnDataShare").click(function () {
    $("#DataShareWarning").show();
    $("#DataShareAccepted").hide();
    $("#DataShareDenied").hide();
    $.ajax(setRequestDocId(access_token, $("#fname").val())).done(function (response) {
        console.log("DocId Protocol Success");
        console.log(response);
        DocIdProtocol = response.protocol
        $("#screen_data_share").fadeIn("slow", function () {
            // Animation complete
        });
    }).fail(function (response) {
        console.log("DocId Protocol fail");
        console.log(response);
    });
});

$("#btn_data_share_ok").on("click", function () {
    $.ajax(setRefeshTokenSettings(refresh_token))
        .done(function (response) {
            console.log("Refresh Token Success: ");
            console.log(response);
            refresh_token = response.refresh_token;
            access_token = response.access_token;
            token_type = response.token_type;

            $.ajax(setCallbackSettings(access_token, $("#fname").val())).done(function (response) {
                console.log("User data Success");
                console.log(response);
                $("#UserDocId").val(response.DocId);
                $("#Username").val(response.name);
                $("#UserAddress").val(response.address);
                $("#UserTax").val(response.tax);

                var ValorPedido = parseInt($("#lname").val());

                $("#UserCreditOptions").html("");

                for (var i = 2; i < 6; i++) {
                    var radioBtn = $("<label> R$" + (ValorPedido + ((ValorPedido / 100 * response.tax) * i)) +
                        " in " + i + "X with " + response.tax + "% rate </label><input type='radio' value='"
                        + (ValorPedido + ((ValorPedido / 100 * response.tax) * i)) +
                        " in " + i + "X with " + response.tax +
                        " % rate' name='rbtnCount' /><br>");
                    radioBtn.appendTo('#UserCreditOptions');
                }

                $("#screen_data_share").fadeOut("fast", function () {
                    $("#DataShareDenied").hide();
                    $("#DataShareWarning").hide();
                    $("#DataShareAccepted").show();
                    $("#formCredit").show();
                    $("#StatusSearching").hide();
                });
            }).fail(function (response) {
                console.log("User data fail");
                console.log(response);
            })

            $.ajax(setPathConfirmSettings(access_token, $("#fname").val(), DocIdProtocol)).done(function (response) {
                console.log("Patch Confirm Phone Success");
                console.log(response);
            }).fail(function (response) {
                console.log("Patch Confirm Phone Fail");
                console.log(response)
            });


        })
        .fail(function (response) {
            console.log("Refresh Token fail: ");
            console.log(response);
        });

});

$("#btn_data_share_cancel").on("click", function () {
    $.ajax(setRefeshTokenSettings(refresh_token))
        .done(function (response) {
            console.log("Refresh Token Success: ");
            console.log(response);
            refresh_token = response.refresh_token;
            access_token = response.access_token;
            token_type = response.token_type;

            $.ajax(setDeleteDocIdSettings(access_token, $("#fname").val(), DocIdProtocol)).done(function (response) {
                console.log("Delete Confirm Phone Success");
                console.log(response);
            }).fail(function (response) {
                console.log("Delete Confirm Phone Fail");
                console.log(response)
            });


        });

    $("#screen_data_share").fadeOut("fast", function () {
        $("#screen_credit_confirm").hide();
        $("#DataShareWarning").hide();
        $("#DataShareDenied").show();
    });
});

$("#btnConfirmCredit").on("click", function () {
    $.ajax(setRefeshTokenSettings(refresh_token))
        .done(function (response) {
            console.log("Refresh Token Success: ");
            console.log(response);
            refresh_token = response.refresh_token;
            access_token = response.access_token;
            token_type = response.token_type;

            $.ajax(setCreditProposalSettings(access_token, 8, 100, 108, $('input[name=rbtnCount]:checked').val() + "%")).done(function (response) {
                console.log("Send Proposal Success: ");
                console.log(response);

                ProposalProtocol = response.analysisProtocol;

                $("#ProposalWarning").show();
            });
        });

    $("#screen_credit_confirm p").text("The Teros Retail is requesting" +
        "confirmation of the purchase of credit in the amount of:" + $('input[name=rbtnCount]:checked').val() + "%")
    $("#screen_credit_confirm").show();
});

$("#btn_credit_confirm_ok").on("click", function () {
    $("#screen_credit_confirm").hide();
    $("#ProposalWarning").hide();
    $("#ProposalAccepted").show();
    $.ajax(setRefeshTokenSettings(refresh_token))
        .done(function (response) {
            console.log("Refresh Token Success: ");
            console.log(response);
            refresh_token = response.refresh_token;
            access_token = response.access_token;
            token_type = response.token_type;
            
            $.ajax(setPatchProposalSettings(access_token, 8, 100, 108, $('input[name=rbtnCount]:checked').val() + "%", ProposalProtocol))
                .done(function (response) {
                    console.log("Patch Proposal Success");
                    console.log(response);
                })
                .fail(function (response) {
                    console.log("Patch Proposal fail");
                    console.log(response);
                });
        });
    
    $("#btnPrintInvoice").show();
});

$("#btn_credit_confirm_cancel").on("click", function () {
    $.ajax(setRefeshTokenSettings(refresh_token))
        .done(function (response) {
            console.log("Refresh Token Success: ");
            console.log(response);
            refresh_token = response.refresh_token;
            access_token = response.access_token;
            token_type = response.token_type;

            $.ajax(setDeleteDocIdSettings(access_token, $("#fname").val(), DocIdProtocol)).done(function (response) {
                console.log("Delete Confirm Phone Success");
                console.log(response);
            }).fail(function (response) {
                console.log("Delete Confirm Phone Fail");
                console.log(response)
            });


        });

    $("#screen_data_share").fadeOut("fast", function () {
        $("#screen_credit_confirm").hide();
        $("#DataShareWarning").hide();
        $("#DataShareDenied").show();
    });
});



$("#btnPrintInvoice").on("click", function () {
    $.ajax(setCallbackProposalSettings(access_token, ProposalProtocol)).done(function (response){
        console.log("Callback Proposal Success");
        console.log(response);

        $("#InvoiceProtocol").text(ProposalProtocol);
        $("#InvoiceDocId").text($("#fname").val());
        $("#InvoiceName").text(response.name);
        $("#InvoiceCredit").text($("lname").val());
        $("#InvoiceBank").text($('#Banco').val());
        $("#InvoiceTax").text(response.tax);
        $("#InvoiceAmmount").text(response.amountTax);
        $("#InvoiceComment").text($('input[name=rbtnCount]:checked').val() + "%");
        $("#ModalPrintInvoice").show();
    })
    .fail(function(response){
        alert("Erro em imprimir o pedido");
    });
})





// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
$("#btnTerms").on("click", function () {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
});

// When the user clicks on <span> (x), close the modal
$(".close").on("click", function () {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";

    modal = document.getElementById("ModalPrintInvoice");
    modal.style.display = "none";
})

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    var modal = $("#myModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }

    modal = $("#ModalPrintInvoice");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }