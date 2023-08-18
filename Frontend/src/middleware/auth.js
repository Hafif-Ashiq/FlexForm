export default function auth({ next, router }) {
    console.log('here');
    if (!localStorage.getItem('token')) {
      return router.push({ name: 'Sign In' });
    }
  
    return next();
  }