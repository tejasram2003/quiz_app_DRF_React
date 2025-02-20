import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { listQuizzes } from '../../actions/QuizActions';
import { Card, Spinner, Alert, Container, Row, Col } from 'react-bootstrap';
import { PencilSquare } from 'react-bootstrap-icons';

function HomeScreen() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const userLogin = useSelector(state => state.userLogin);
    const { userInfo } = userLogin;

    const quizList = useSelector(state => state.quizList);
    const { error, loading, quizzes } = quizList;

    // ✅ Fetch quizzes when component mounts
    useEffect(() => {
        if (userInfo) {
            dispatch(listQuizzes());
        }
    }, [dispatch, userInfo]);

    return (
        <Container>
            {userInfo ? (
                <> {/* ✅ Wrap in Fragment */}
                    <h1 className="my-4 text-center">Quizzes Dashboard</h1>

                    <button className="btn btn-primary mb-4" onClick={() => navigate('/create')}>
                        Create New Quiz
                    </button>

                    {/* 🔄 Show Loading Spinner */}
                    {loading && (
                        <div className="d-flex justify-content-center my-4">
                            <Spinner animation="border" role="status">
                                <span className="visually-hidden">Loading...</span>
                            </Spinner>
                        </div>
                    )}

                    {/* ⚠️ Show Error Message if API Fails */}
                    {error && <Alert variant="danger">{error}</Alert>}

                    {/* ✅ Display Quiz List */}
                    <Row>
                        {quizzes?.map((quiz) => (
                            <Col key={quiz.id} md={4} className="mb-4">
                                <Card className="shadow-sm position-relative">
                                    <Card.Body>
                                        {/* ✏️ Edit Button (Top Right) */}
                                        <button
                                            className="btn btn-light position-absolute top-0 end-0 m-2"
                                            onClick={() => navigate(`/quiz/${quiz.id}/edit`)}
                                            style={{ border: "none" }}
                                        >
                                            <PencilSquare size={20} className="me-1" />
                                            Edit
                                        </button>

                                        <Card.Title>{quiz.title}</Card.Title>
                                        <Card.Text>{quiz.description}</Card.Text>
                                        <Card.Text className="text-muted">
                                            {new Date(quiz.created_at).toLocaleDateString()}
                                        </Card.Text>

                                        <Card.Footer>
                                            <button className="btn btn-primary" onClick={() => navigate(`/quiz/${quiz.id}`)}>
                                                View Submissions
                                            </button>
                                        </Card.Footer>
                                    </Card.Body>
                                </Card>
                            </Col>
                        ))}
                    </Row>
                </>
            ) : (
                <h1 className="my-4 text-center">Please Login to view Quizzes</h1>
            )}
        </Container>
    );
}

export default HomeScreen;
