import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# Step 1: Load and preprocess the dataset
def load_and_preprocess(file_path):
    """
    Load dataset and prepare features and target.
    TODO:
    - Read CSV file
    - Separate features (X) and target (y)
    - Identify numerical and categorical columns
    - Create preprocessing pipelines
    - Return X, y, and preprocessor
    """

    df = pd.read_csv(file_path)

    numerical_features = ['Marketing_Spend','R&D_Spend', 'Administration_Costs', 'Number_of_Employees']

    # handle_unknown = 'ignore' prevents crashes if a region is unexpected

    preprocessor = ColumnTransformer([
        ('num',StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), ['Region'])
    ])

    X = df.drop('Revenue', axis = 1)

    y = df['Revenue']
    
    return X, y, preprocessor

# Step 2: Train the Linear Regression model
def train_model(X_train, y_train, preprocessor):
    """
    Train Linear Regression using a pipeline.
    TODO:
    - Create pipeline with preprocessor + LinearRegression
    - Fit model on training data
    - Return trained model
    """

    # TODO: model = Pipeline([...])
    # TODO: model.fit(X_train, y_train)


    model = Pipeline([
        ('pre', preprocessor),
        ('reg', LinearRegression())
    ])

    model.fit(X_train, y_train)
    return model


# Step 3: Evaluate model performance
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.
    TODO:
    - Generate predictions
    - Calculate MAE, RMSE, R²
    - Print evaluation metrics
    """

    # TODO: y_pred = model.predict(X_test)
    # TODO: compute evaluation metrics
    
    y_pred = model.predict(X_test)
    print('MAE:', mean_absolute_error(y_test, y_pred))
    print('RMSE:', mean_squared_error(y_test, y_pred, squared = False))
    print('R2:', r2_score(y_test,y_pred))


# Step 4: Predict revenue for new input
def predict_revenue(model, user_input):
    """
    Predict revenue for a single user input.
    TODO:
    - Convert input dictionary to DataFrame
    - Predict revenue
    - Display result
    """
    # TODO: input_df = pd.DataFrame([user_input])
    # TODO: model.predict(input_df)
    user_df = pd.DataFrame([user_input], columns = ['Marketing_Spend','R&D_Spend', 'Administration_Costs', 'Number_of_Employees','Region'])
    pred = model.predict(user_df)
    print('Predicted Revenue: {:.2f}'.format(pred[0]))



# Step 5: Main program
def main():
    """
    Main execution flow.
    TODO:
    - Load and preprocess data
    - Split into train and test sets
    - Train model
    - Evaluate model
    - Accept user input in loop and predict revenue
    """

    X, y, preprocessor = load_and_preprocess('data.csv')
    X_train, X_test,y_train,y_test = train_test_split(X, y, test_size= 0.2, random_state = 42)
    model = train_model(X_train, y_train, preprocessor)
    evaluate_model(model, X_test, y_test)


    try:
        while True:
            region = input('Enter company region (Northn America/Europe/Asia or exit to stop): ')
            if region.lower() == 'exit' :
                print('Exiting the Program. Goodbye')
                break
            
            region = region.strip().title()
            if region not in ['North America', 'Europe', 'Asia']:
                print('Invalid Region. Please Enter One of : North America, Europe, Asia.\n')
                continue

            try: 
                m = float(input('Marketing_Spend: '))
                r = float(input('R&D_Spend: '))
                a = float(input('Administration_Costs: '))
                n = float(input('Number_of_Employees: '))

            except ValueError:
                print('Please enter valid Numbers for all Expenditures. \n')
                continue

            # Use a Dictionary mapping keys to values for reliable DataFrame parsing

            user_input = {
                'Marketing_Spend' : m,
                'R&D_Spend' : r,
                'Administration_Costs' : a,
                'Number_of_Employees' : n,
                'Region' : region
            }

            predict_revenue(model, user_input)

    except EOFError:
        print('Input ended. Exiting The Program.')


        
      

if __name__ == "__main__":
    main()