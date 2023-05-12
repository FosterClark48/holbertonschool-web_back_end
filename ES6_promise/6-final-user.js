import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// helper function because YOU CAN'T NEST TERNARY EXPRESSIONS APPARENTLY
function getPromiseResult(result) {
  if (result.status === 'fulfilled') {
    return result.value;
  }
  if (result.reason) {
    return result.reason.toString();
  }
  return 'Unkown error';
}

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPhotoPromise = uploadPhoto(fileName);

  return Promise.allSettled([signUpPromise, uploadPhotoPromise])
    .then((results) => results.map((result) => ({
      status: result.status,
      value: getPromiseResult(result),
    })));
}
