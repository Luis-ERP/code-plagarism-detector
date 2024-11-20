import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import joblib

def evaluate_model(model_path, vectorizer_path, test_X, test_y, report_csv_path, confusion_matrix_path):
    # Load the trained Random Forest model and TF-IDF vectorizer
    clf = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    # Predict the test data
    y_pred = clf.predict(test_X)

    # Generate and save the classification report as CSV
    report = classification_report(test_y, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    report_df.to_csv(report_csv_path, index=True)
    print(f"Classification report saved to {report_csv_path}")

    # Generate the confusion matrix
    cm = confusion_matrix(test_y, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)

    # Plot and save the confusion matrix as an image
    disp.plot(cmap=plt.cm.Blues, xticks_rotation='vertical')
    plt.title('Confusion Matrix')
    plt.savefig(confusion_matrix_path, dpi=300)
    plt.close()
    print(f"Confusion matrix saved to {confusion_matrix_path}")

if __name__ == "__main__":
    # Load model and vectorizer
    model_path = r'RF\random_forest_model.pkl'
    vectorizer_path = r'RF\tfidf_vectorizer.pkl'
    
    # Load vectorizer
    vectorizer = joblib.load(vectorizer_path)
    
    # Option 1: Load preprocessed test data (already vectorized)
    test_X, test_y = joblib.load(r'RF\test_data.pkl')
    
    # Evaluate the model
    evaluate_model(model_path, vectorizer_path, test_X, test_y, 
                   r'RF\classification_report.csv', r'RF\confusion_matrix.png')