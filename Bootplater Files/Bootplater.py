import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    # loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    loader = FileSystemLoader(os.path.join(PATH)),
    trim_blocks=False)


def render_template(template_filename, context):
        return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)



def render(template_path, context):
        path, filename = os.path.split(template_path)
        return Environment(
            loader= FileSystemLoader(path or './')
        ).get_template(filename).render(context)


def create_index_html():
        fname = "output.html"
        urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
        context = {
            'urls': urls
        }
        #
        with open(fname, 'w') as f:
            html = render_template('index.html', context)
            f.write(html)


def generate_naved_template(left_link_names, right_link_names, item_number, checker, site_name = "WRITE-SITE-NAME-HERE!"):
                # file_name = 'output_template.html'

              combined_link_names = left_link_names + right_link_names

              context = {
                                'left_link_names' : left_link_names,
                                'right_link_names' : right_link_names,
                                'site_name' : site_name,
                                'item_number' : item_number,
                                'left_list_size' : len(left_link_names),
                                'right_link_index' : ((item_number) - len(left_link_names) ),
                                'combined_link_names' : combined_link_names,
                                'checker' : checker,

                          }




              html = render('nav-bar.html', context) #eikhane continue korba
              return(html)



def html_file_maker(html, name):
    file_name = name + ".html"
    file = open(file_name,'w')
    file.write(html)
    file.close()


def generate_template_package(left_link_names, right_link_names, site_name= "WRITE_SITE_NAME"):
    combined_list = left_link_names + right_link_names


    for item in range(len(combined_list)):
        if (item >= len(left_link_names)):
            checker = True
        else:
            checker = False
        html = generate_naved_template(left_link_names, right_link_names, checker=checker, item_number= item, site_name= site_name)
        html_file_maker(html, combined_list[item])



def completion_message():
    print("Done!")
    print("Your HTML Files have been generated!")



def main(left_link_names, right_link_names, site_name):
        generate_template_package(left_link_names, right_link_names, site_name)
        completion_message()



# A More Direct Approach - COMMENT OUT INTERACTIVE WIZARD (START TO END) AND UNCOMMENT THIS TO RUN DIRECTLY
# left_link_names = ['Home', 'Link 1', 'Link 2']
# right_link_names = ['About Us', 'Log In', 'Sign Up']
# site_name = "TryOut!"


# Interactive Wizard - START
number_of_links = input("Please enter the number of items in your navbar: ")

number_of_left_links = input("Please enter how many of the " + number_of_links + " is in the left navbar: ")

number_of_links = int(number_of_links)
number_of_left_links = int(number_of_left_links)
number_of_right_links = number_of_links - number_of_left_links

left_link_names = []
right_link_names = []
site_name = ""

for i in range(0, number_of_left_links):
    value = input("Please enter the " + str(i + 1) + "th left nav item: ")
    left_link_names.append(value)



for i in range(0, number_of_right_links):
    value = input("Please enter the " + str(i + 1) + "th left nav item: ")
    right_link_names.append(value)


site_name = input("Please enter the name of your site: ")

# Interactive Wizard - END


if __name__ == "__main__":
    main(left_link_names=left_link_names, right_link_names=right_link_names, site_name=site_name)
