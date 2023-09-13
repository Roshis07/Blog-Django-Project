from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Roshis",
        "date": date(2022, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Nature encompasses the vast and intricate tapestry of the natural world, comprising everything untouched and unaltered by human hands. It is the embodiment of Earth's inherent beauty, diversity, and complexity, showcasing a dazzling array of life forms, landscapes, and ecosystems. Within the realm of nature, one can discover the rich tapestry of biodiversity, where countless species, from microscopic organisms to majestic creatures, inhabit the various corners of our planet, each intricately woven into the intricate web of life. Nature's landscapes range from the breathtaking majesty of towering mountains and lush forests to the stark beauty of arid deserts and expansive grasslands, all shaped by geological processes and climatic conditions. Ecosystems, both microscopic and immense, function as interconnected communities, where living organisms and their physical surroundings harmonize in delicate equilibrium.

The natural world also orchestrates the ebb and flow of weather patterns, the evolution of climate, and the occurrence of awe-inspiring natural events like earthquakes, hurricanes, and celestial phenomena. Amid growing environmental concerns, there is an increasing emphasis on the conservation and preservation of nature, recognizing its intrinsic value and the critical role it plays in sustaining life on our planet. Beyond its ecological significance, nature offers sol



        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Roshis",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Mountains stand as majestic giants on the Earth's surface, their towering peaks reaching towards the sky, as if yearning to touch the heavens. These natural wonders are the result of geological forces and millennia of shaping, bearing witness to the ever-changing narrative of our planet. They command awe and respect, not only for their sheer size but for the remarkable biodiversity they harbor, from the hardy vegetation clinging to their slopes to the elusive creatures that call these heights home.        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Roshis",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          
Nature encompasses the boundless tapestry of the Earth's unaltered landscapes, the intricate web of life it sustains, and the profound beauty and harmony found within its realms. It is a testament to the sheer diversity and resilience of life, as well as the geological and ecological processes that have shaped our planet over eons. Nature is a living, breathing entity, a symphony of ecosystems, species, and phenomena that inspire wonder and reverence.
        """
    }
]

def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })
