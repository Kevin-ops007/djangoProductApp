# Django Product Search and Filter Project

This project is a simple product listing and filtering application built using Django. It allows users to search and filter products by description, category, and tags. The project demonstrates basic CRUD operations, model relationships, and search and filtering functionality using Django's ORM. Additionally, it uses Django Bootstrap for styling the frontend interface. Also the sample data is populated using the Django admin panel.

## Getting Started

### Prerequisites

Ensure that you have Python installed on your machine. You will also need to install the dependencies listed in the `requirements.txt` file.

### Installation

1. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```
2. **Go to Project Directory**
   ```bash
   cd productsProject
   ```
3. **Run Project**
   ```bash
   python manage.py runserver
   ```
   The project should now be running on `http://loacalhost:8000`.

### Styling

The project uses Django Bootstrap for styling, providing a responsive and user-friendly interface for searching and filtering products.

### Usage

- **Search**: Use the search bar to filter products based on their descriptions.
- **Filter by Category**: Select a category from the dropdown menu to filter products belonging to that category.
- **Filter by Tags**: Check the boxes next to tags to filter products based on associated tags.
- **Clear Filters**: Use the "Clear" button to reset all filters and display the full list of products.
  Liberties Taken
- **Category and Tags**: For simplicity, it is assumed that categories and tags only have a name property, without an ID field for filtering purposes.
- **Product Model**: The Product model includes only the following fields:
  - **name**: Name of the product.
  - **description**: Description of the product.
  - **category**: Foreign key linking to a Category object.
  - **tags**: Many-to-many relationship with Tag objects.
  - **image**: An image field to store product images.
    These assumptions were made to streamline the project and demonstrate basic functionality without introducing unnecessary complexity.
