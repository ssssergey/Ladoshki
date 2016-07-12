$(document).ready(function () {
    $("form#search").submit(function () {
        text = $("#id_q").val();
        if (text == "" || text == "Поиск") {
// if empty, pop up alert
            alert("Укажите, что Вы хотите найти.");
// halt submission of form
            return false;
        }
    });

    jQuery("#submit_review").click(addProductReview);
    jQuery("#review_form").addClass('hidden');
    jQuery("#add_review").click(slideToggleReviewForm);
    jQuery("#add_review").addClass('visible');
    jQuery("#cancel_review").click(slideToggleReviewForm);


});

// toggles visibility of "write review" link
// and the review form.
function slideToggleReviewForm() {
    jQuery("#review_form").slideToggle();
    jQuery("#add_review").slideToggle();
    jQuery("#review_form").removeClass();
    jQuery("#add_review").removeClass();
}

function addProductReview(e) {
    e.preventDefault();
// build an object of review data to submit
    var review = {
        title: jQuery("#id_title").val(),
        content: jQuery("#id_content").val(),
        rating: jQuery("#id_rating").val(),
        slug: jQuery("#id_slug").val(),
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
    };
// make request, process response
    url = "/review/product/add/";
    //jQuery.post(url, review,
    //    function (response) {
    //        jQuery("#review_errors").empty();
    //        if (response.success == "True") {
    //            jQuery("#submit_review").attr('disabled', 'disabled');
    //            jQuery("#no_reviews").empty();
    //            jQuery("#reviews").prepend(response.html).slideDown();
    //            new_review = jQuery("#reviews").children(":first");
    //            new_review.addClass('new_review');
    //            jQuery("#review_form").slideToggle();
    //        }
    //        else {
    //            jQuery("#review_errors").append(response.html);
    //        }
    //    }, "json");

    $.ajax({
        url: url,
        type: "POST",
        data: review,
        //data: {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
        dataType: "json",
        success: function (response) {
            jQuery("#review_errors").empty();
            if (response.success == "True") {
                jQuery("#submit_review").attr('disabled', 'disabled');
                jQuery("#no_reviews").empty();
                jQuery("#reviews").prepend(response.html).slideDown();
                new_review = jQuery("#reviews").children(":first");
                new_review.addClass('new_review');
                jQuery("#review_form").slideToggle();
            }
            else {
                jQuery("#review_errors").append(response.html);
            }
        }
    });
}

$(window).on("load", function () {
    equalHeight($(".thumbnail"));
});

function equalHeight(group) {
    var tallest = 0;
    group.each(function () {
        var thisHeight = $(this).height();
        if (thisHeight > tallest) {
            tallest = thisHeight;
        }
    });
    group.each(function () {
        $(this).height(tallest);
    });
}

