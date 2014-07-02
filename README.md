# Where to find the docs:

http://unboundedrobotics.github.io/ubr1_preview

# How to generate the docs:

    git clone -b documentation https://github.com/unboundedrobotics/ubr1_preview.git ubr1_preview
    cd ubr1_preview; make html; cd ..
    git clone -b gh-pages https://github.com/unboundedrobotics/ubr1_preview.git gh_pages
    cp -r ubr1_preview/_build/html/* gh_pages/
    cd gh_pages; git add *; git commit -m "updating"; git push origin gh-pages
